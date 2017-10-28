#!/usr/bin/python3
import datetime
import calendar
import locale

locale.setlocale(locale.LC_ALL, 'sv_SE.utf8')

now = datetime.datetime.now()

week = now.isocalendar()[1]
weekday = list(calendar.day_abbr)[now.weekday()]
date = now.day
month = calendar.month_abbr[now.month]

print("v" + str(week) + ", " + weekday + " " + str(date) + " " + month)
