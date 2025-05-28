import cups
import os
import time

arquivo = "/home/administrador/code/python/print/arquivo.pdf"
printer_name = "Samsung_M4080FX"

# Esperar o arquivo existir
tentativas = 5
while not os.path.exists(arquivo) and tentativas > 0:
    time.sleep(1)
    tentativas -= 1

if os.path.exists(arquivo):
    conn = cups.Connection()
    conn.printFile(printer_name, arquivo, "Meu Job", {})
    print("Arquivo enviado para impressão.")
else:
    print(f"Arquivo não encontrado: {arquivo}")
