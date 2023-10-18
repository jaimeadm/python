# https://sites.google.com/view/andersontecnologia/ubuntu/instalando-o-locale-pt_br-utf-8
# sudo locale-gen pt_BR.UTF-8
# locale para internacionalização

import calendar
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

print(calendar.calendar(2023))
print(locale.getlocale())
