# module used to work with dates and times

import datetime
import pytz #Timezone

for each in (dir(datetime)):
    print(each)

ist = pytz.timezone('Asia/Kolkata')

print(datetime.datetime.now())
print(datetime.datetime.today())
print(datetime.datetime.now(ist))
print(datetime.datetime.now().year)
print(datetime.datetime.now().month)
print(datetime.datetime.now().day)
print(datetime.datetime.now().hour)
print(datetime.datetime.now().minute)
print(datetime.datetime.now().second)
print(datetime.datetime.now().strftime('%y-%m-%d'))


import os
my_path = r'C:\git_repos'
tm = os.path.getmtime(my_path) #Timestamp object
tc = os.path.getctime(my_path) #Timestamp object
print(datetime.datetime.fromtimestamp(tm)) #Time modify
print(datetime.datetime.fromtimestamp(tm)) #Time Created

