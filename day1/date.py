from datetime import datetime,date,timedelta
#current time and date
now=datetime.now()
print("Current datetime",now)
#only date
print("Todays date",date.today())
#fomatted datetime

formatted = now.strftime("%d-%m-%Y %H:%M:%S")
print("Formatted datetime",formatted)
#parsed datetime
date_str="04-02-2005  14:55:00"
parsed=datetime.strptime(date_str,"%d-%m-%Y %H:%M:%S")
print("Parsed date:",parsed)
#timedelta
tomorrow=now+timedelta(days=1)
print("Tomorrow:",tomorrow)
yesterdays=now-timedelta(days=1)
print("Yesterday:",yesterdays)
ftime=now+timedelta(hours=3,minutes=30)
print("Ftime:",ftime)

now=datetime.now()
format_12hr=now.strftime("%d/%m/%Y %T:%M:%S")
print(format)