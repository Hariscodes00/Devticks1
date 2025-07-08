import datetime
from time import strftime

import pytz
d = datetime.date.today()
print(d)
print(d.weekday())
print(d.isoweekday())
td= datetime.timedelta(days=84)
tday = datetime.date(2025,7,8)
print(tday-td)
bday = datetime.date(2025,8,23)
tillbday = bday-tday
print(tillbday.total_seconds())

utc_now = datetime.datetime.now(tz=pytz.UTC)
print(utc_now)
for tzs in pytz.all_timezones:
    print(tzs)
dt_mtn = datetime.datetime.now()
dtz = dt_mtn.astimezone(pytz.timezone('Australia/Brisbane' ))
print(dtz)

print(dt_mtn.strftime('%B  %d , %Y'))
dt_str = 'July  08 , 2025'
ds = dt_mtn.strptime(dt_str ,'%B  %d , %Y')
print(ds)