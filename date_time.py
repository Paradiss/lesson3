from datetime import datetime, date, time, timedelta
#import locale

#locale.setlocale(locale.LC_TIME, "ru_Ru")

today = datetime.now()
delta1 = timedelta(days=1)
delta2 = timedelta(days=30)

print(today-delta1)
print(today)
print(today-delta2)
str_for_date = '01/01/17 12:10:03.234567'
date_from_str = datetime.strptime(str_for_date, '%d/%m/%y %H:%M:%S.%f')
print(date_from_str)