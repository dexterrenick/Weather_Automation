"""
weather.py
Texts my phone weather every morning
@author Dexter Renick
@Version 6/26/18
"""
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import os
import smtplib

def getweather(location, myurl):
    uClient = uReq(myurl)
    #creates a variable for html of entire website
    page_html = uClient.read()
    uClient.close()

    #creates readable html version of entire website
    pagesoup = soup(page_html, "html.parser")

    #finds the highs and lows of the day
    high_low_string = str(pagesoup.findAll("span",{"class":"Va(m) Px(6px)"}))
    weather_high = ((high_low_string)[70:72])
    weather_low = ((high_low_string)[214:216])

    #finds what it feels like temperature
    feels_like_string = str(pagesoup.findAll("div",{"class":"D(tbc) W(60%)"}))
    print(feels_like_string)

    return ("Today in " + location + " you can expect a high of " + weather_high + " and a low of " + weather_low + ".")

def sendtext(messege):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("login email", "password")
    msg = (messege)
    server.sendmail("login email", "target email", msg)
    server.quit()

def main():
    weather = getweather("Pasadena", "https://www.yahoo.com/news/weather/united-states/pasadena/pasadena-2468964")
    sendtext(weather)
    weather = getweather("Los Angeles", "https://www.yahoo.com/news/weather/united-states/los-angeles/los-angeles-2442047")
    sendtext(weather)
    weather = getweather("Sun Valley", "https://www.yahoo.com/news/weather/united-states/sun-valley/sun-valley-2501907")
    sendtext(weather)



if __name__ == '__main__':
    main()
