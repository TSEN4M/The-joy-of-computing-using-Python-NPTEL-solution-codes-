from datetime import datetime as dt
import pytz

time_zones=pytz.all_timezones

for i in range(len(time_zones)):
     zone=time_zones[i]
     tz=pytz.timezone(zone)   #creating a special object tz which has each timezones as zones
     print('Current time at zone ',zone,' is ',dt.now(tz))