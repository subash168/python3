# date module
import datetime as dt
new=dt.date(2022,11,24)# create a date
print(new)
print("year",new.year)
print("month",new.month)
print("day",new.day)
import time
print(time.localtime(time.time()))# now loaal time
print(time.time())

current=dt.datetime.now()# create date time
new=dt.datetime(2024,9,11)
diff=new-current # difference in current and new date 
print(diff)

current_time=dt.datetime.now()# string format time
s=current_time.strftime("%A,%B,%d,%y")
print(s)

