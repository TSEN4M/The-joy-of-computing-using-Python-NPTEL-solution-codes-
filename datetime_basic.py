#current date_time
from datetime import datetime as dt
print('the current system datetime is: ',dt.now())

#time zone
import pytz
tz=pytz.timezone('singapore')
print('Singapore time zone :',dt.now(tz))
print()
print('All the time zones available in pytz are :')
print(pytz.all_timezones)
print('total time zones available is : ',len(pytz.all_timezones))

#calculating day with a date
import calendar
print('the day is :',calendar.weekday(2018,7,6))
print('the day is : ',calendar.weekday(2022,4,16))

#time.time return the current time in miliseconds since jan 1 1970
year=2022
print(calendar.prcal(year))