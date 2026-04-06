import os
import time
import csv
import io
import threading
import requests
from flask import Flask, Response
from prometheus_client import Gauge, generate_latest, CONTENT_TYPE_LATEST

TENANT_ID = os.getenv("TENANT_ID")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
SCRAPE_INTERVAL_SECONDS = int(os.getenv("SCRAPE_INTERVAL_SECONDS", "300"))
REPORT_PERIOD = os.getenv("REPORT_PERIOD", "D7")

if not all([TENANT_ID, CLIENT_ID, CLIENT_SECRET]):
    raise SystemExit(
        "Faltam variáveis TENANT_ID, CLIENT_ID, CLIENT_SECRET no .env")

TOKEN_URL = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token"
SCOPE = "https://graph.microsoft.com/.default"
REPORT_URL = f"https://graph.microsoft.com/v1.0/reports/getEmailActivityCounts(period='{REPORT_PERIOD}')"

app = Flask(__name__)

# Métricas (Gauge porque o relatório traz valores agregados por dia/intervalo)
emails_sent = Gauge("exchange_emails_sent",
                    "Emails sent (per day in report)", ["date"])
emails_received = Gauge("exchange_emails_received",
                        "Emails received (per day in report)", ["date"])
emails_read = Gauge("exchange_emails_read",
                    "Emails read (per day in report)", ["date"])
emails_deleted = Gauge("exchange_emails_deleted",
                       "Emails deleted (per day in report)", ["date"])

last_success = Gauge("exchange_exporter_last_success_unixtime",
                     "Last successful refresh (unix time)")
up = Gauge("exchange_exporter_up", "Exporter up (1=ok, 0=error)")

_token_cache = {"access_token": None, "expires_at": 0}


def get_token() -> str:
    now = int(time.time())
    if _token_cache["access_token"] and now < _token_cache["expires_at"] - 60:
        return _token_cache["access_token"]

    data = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "grant_type": "client_credentials",
        "scope": SCOPE,
    }
    r = requests.post(TOKEN_URL, data=data, timeout=20)
    r.raise_for_status()
    payload = r.json()
    _token_cache["access_token"] = payload["access_token"]
    _token_cache["expires_at"] = now + int(payload.get("expires_in", 3599))
    return _token_cache["access_token"]


def parse_report_csv(text: str):
    """
    Retorno do endpoint /reports vem como CSV em texto.
    Campos típicos: Report Refresh Date, Send Count, Receive Count, Read Count, Delete Count
    """
    # Limpa métricas anteriores (para evitar acumular labels antigas)
    emails_sent.clear()
    emails_received.clear()
    emails_read.clear()
    emails_deleted.clear()

    f = io.StringIO(text)
    reader = csv.DictReader(f)

    # Possíveis nomes (podem variar levemente, então tratamos com fallback)
    for row in reader:
        # Geralmente: "Report Refresh Date"
        date = row.get("Report Refresh Date") or row.get(
            "Date") or row.get("reportRefreshDate") or "unknown"

        def to_int(v):
            try:
                return int(float(v))
            except Exception:
                return 0

        send = to_int(row.get("Send Count") or row.get(
            "Send") or row.get("sendCount"))
        recv = to_int(row.get("Receive Count") or row.get(
            "Receive") or row.get("receiveCount"))
        read = to_int(row.get("Read Count") or row.get(
            "Read") or row.get("readCount"))
        dele = to_int(row.get("Delete Count") or row.get(
            "Delete") or row.get("deleteCount"))

        emails_sent.labels(date=date).set(send)
        emails_received.labels(date=date).set(recv)
        emails_read.labels(date=date).set(read)
        emails_deleted.labels(date=date).set(dele)


def refresh_loop():
    while True:
        try:
            token = get_token()
            headers = {"Authorization": f"Bearer {token}"}
            r = requests.get(REPORT_URL, headers=headers, timeout=30)
            r.raise_for_status()

            parse_report_csv(r.text)

            up.set(1)
            last_success.set(int(time.time()))
        except Exception as e:
            up.set(0)
            import traceback
            print("ERROR refresh_loop:", repr(e), flush=True)
            traceback.print_exc()
        time.sleep(SCRAPE_INTERVAL_SECONDS)


@app.get("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)


@app.get("/health")
def health():
    return {"ok": True}, 200


if __name__ == "__main__":
    t = threading.Thread(target=refresh_loop, daemon=True)
    t.start()
    app.run(host="0.0.0.0", port=8000)
