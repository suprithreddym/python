# import time
#
# print("the epoch on the system starts at " + time.strftime('%c', time.gmtime(0)))
#
# print("The current time zone is {} with an offset {}".format(time.tzname[0], time.timezone))
#
# if time.daylight != 0:
#     print("\tDaylight saving time is in effect for your location")
#     print("\t DST time zone is " + time.tzname[1])
#
# print("local time is " + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
# print("UTC time is " + time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()))


import datetime

print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.utcnow())