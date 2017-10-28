#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import datetime

now = datetime.datetime.now()
hour = now.hour
minute = now.minute
adj = "" # init variable

if minute >= 23:
    hour += 1

    if hour == 24:
        hour = 0

if hour == 1 or hour == 13:
    time_hour = "ett"
elif hour == 2 or hour == 14:
    time_hour = "två"
elif hour == 3 or hour == 15:
    time_hour = "tre"
elif hour == 4 or hour == 16:
    time_hour = "fyra"
elif hour == 5 or hour == 17:
    time_hour = "fem"
elif hour == 6 or hour == 18:
    time_hour = "sex"
elif hour == 7 or hour == 19:
    time_hour = "sju"
elif hour == 8 or hour == 20:
    time_hour = "åtta"
elif hour == 9 or hour == 21:
    time_hour = "nio"
elif hour == 10 or hour == 22:
    time_hour = "tio"
elif hour == 11 or hour == 23:
    time_hour = "elva"
elif hour == 12 or hour == 00:
    time_hour = "tolv"

if minute >= 3 and minute <= 7:
    adj = "fem över "
elif minute > 7 and minute < 13:
    adj = "tio över "
elif minute >= 13 and minute <= 17:
    adj = "kvart över "
elif minute > 17 and minute < 23:
    adj = "tjugo över "
elif minute >= 23 and minute <= 27:
    adj = "fem i halv "
elif minute > 23 and minute < 37:
    adj = "halv "
elif minute >= 33 and minute <= 37:
    adj = "fem över halv "
elif minute > 37 and minute < 43:
    adj = "tjugo i "
elif minute >= 43 and minute <= 47:
    adj = "kvart i "
elif minute > 47 and minute < 53:
    adj = "tio i "
elif minute >= 53 and minute <= 57:
    adj = "fem i "

if hour == 13 and minute == 37:
    print("1337")
else:
    print(adj + time_hour)
