#!/usr/bin/python3
from bs4 import BeautifulSoup
import urllib

THERMO_EMPTY            = "<span font='FontAwesome'>\uf2cb</span>"
THERMO_QUARTER          = "<span font='FontAwesome'>\uf2ca</span>"
THERMO_HALF             = "<span font='FontAwesome'>\uf2c9</span>"
THERMO_THREE_QUARTERS   = "<span font='FontAwesome'>\uf2c8</span>"
THERMO_FULL             = "<span font='FontAwesome'>\uf2c7</span>"
SNOW                    = "<span font='FontAwesome'>\uf2dc</span>"
BAN                     = "<span font='FontAwesome'>\uf05e</span> "

url = "http://climendo.com/en/weather/sweden/karlskrona-2701713"

page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, "lxml")

span = soup.find_all("span", class_ = "temp")
temp = span[0].string[:-2]

if int(temp) >= 25:                         # 25 - inf
    print("<span color='#F44336'>" + THERMO_FULL + " tvärvarmt</span>")
    print("<span color='#F44336'>" + THERMO_FULL + " tvärvarmt</span>")
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
