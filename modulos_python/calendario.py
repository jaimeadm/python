# 0 = segunda-feira | 6 = domingo

import calendar
# print(calendar.calendar(2023))
# print(calendar.month(2023, 10))

# numero_primeiro_dia, ultimo_dia = calendar.monthrange(
#    2023, 10)  # último dia do mês
# print(list(enumerate(calendar.day_name)))  # dias da semana
# print(calendar.day_name[numero_primeiro_dia])  # dia da semana
# print(calendar.day_name[calendar.weekday(2023, 10, ultimo_dia)])
for week in calendar.monthcalendar(2023, 10):
    # print(week)
    for day in week:
        if day == 0:
            continue
        print(day)
