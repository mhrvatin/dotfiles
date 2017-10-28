#!/usr/bin/python3
from bs4 import BeautifulSoup
import urllib

THERMO_EMPTY = "<span font='FontAwesome'>\uf2cb</span>"
THERMO_QUARTER = "<span font='FontAwesome'>\uf2ca</span>"
THERMO_HALF = "<span font='FontAwesome'>\uf2c9</span>"
THERMO_THREE_QUARTERS = "<span font='FontAwesome'>\uf2c8</span>"
THERMO_FULL = "<span font='FontAwesome'>\uf2c7</span>"
SNOW = "<span font='FontAwesome'>\uf2dc</span>"
BAN = "<span font='FontAwesome'>\uf05e</span> "

url = "https://www.yr.no/sted/Sverige/Blekinge/Karlskrona/time_for_time.html"

yr = urllib.request.urlopen(url)
# catch exception/no internet connection
soup = BeautifulSoup(yr)

table = soup.find_all("table", class_ = "yr-table-hourly")
td = table[0].find_all("td", class_ = "temperature")

temp = td[2].getText()[0:2]

if int(temp) >= 25:                         # 25 - inf
    print("<span color='#F44336'>" + THERMO_FULL + " sjukt varmt</span>")
    print("<span color='#F44336'>" + THERMO_FULL + " sjukt varmt</span>")
elif int(temp) >= 20 and int(temp) < 25:    # 20 - 24
    print("<span color='#F44336'>" + THERMO_THREE_QUARTERS + " varmt</span>")
    print("<span color='#F44336'>" + THERMO_THREE_QUARTERS + " varmt</span>")
elif int(temp) >= 15 and int(temp) < 20:    # 15 - 19
    print("<span color='#8BC34A'>" + THERMO_HALF + " gött</span>")
    print("<span color='#8BC34A'>" + THERMO_HALF + " gött</span>")
elif int(temp) >= 10 and int(temp) < 15:    # 10 - 14
    print("<span color='#2196F3'>" + THERMO_QUARTER + " kyligt</span>")
    print("<span color='#2196F3'>" + THERMO_QUARTER + " kyligt</span>")
elif int(temp) >= 0 and int(temp) < 10:     # 0 - 9
    print("<span color='#2196F3'>" + THERMO_EMPTY + " kallt</span>")
    print("<span color='#2196F3'>" + THERMO_EMPTY + " kallt</span>")
else:                                       # -inf - 0 
    print("<span color='#2196F3'>" + SNOW + " tvärkallt</span>")
    print("<span color='#2196F3'>" + SNOW + " tvärkallt</span>")
