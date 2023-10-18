from datetime import datetime  # timedelta

# from pytz import timezone
# from dateutil.relativedelta import relativedelta

# data_str = '2022-04-12 09:10:23'
# data_fmt = '%Y-%m-%d %H:%M:%S'
# #data = datetime(2022, 4, 15, 8, 45, 32, tzinfo=timezone('Asia/Tokyo'))
# data = datetime.strptime(data_str, data_fmt)
# print(data)

# data = datetime.now(timezone('America/Sao_Paulo'))
# print(data)

# data = datetime.now()
# print(data.timestamp())
# print(datetime.fromtimestamp(1695738928.556733))

# fmt = '%d/%m/%Y %H:%M:%S'
# data_inicio = datetime.strptime('20/04/1987 09:30:30', fmt)
# data_fim = datetime.strptime('12/12/2022 08:20:20', fmt)
# delta = timedelta(days=10, hours=2)
# delta = relativedelta(data_fim, data_inicio)
# print(delta.days, delta.years)
# print(data_fim + delta)

# print(data_fim)
# print(data_fim + relativedelta(seconds=60, minutes=10))  # + 60s + 10m

# print(data_inicio > data_fim)
# delta = data_fim - data_inicio
# print(delta.days, delta.seconds, delta.microseconds)
# print(delta.total_seconds())

fmt = '%d/%m/%Y'
# data = datetime(2022, 12, 13, 7, 59, 23)
data = datetime.strptime('2022-12-13 07:59:23', '%Y-%m-%d %H:%M:%S')
print(data.strftime(fmt))
print(data.strftime('%Y'), data.year)
