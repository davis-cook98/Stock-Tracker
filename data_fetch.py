#Author Ajay Shah


#Some imports for fetch data via http
from bs4 import BeautifulSoup
import requests
import re


with requests.Session() as c:

      #Asks user for nasdaq symbol and appends it to url for data extraction
      nasdaq_symbol = input("What stock symbol?\n")
      nasdaq_baseurl = 'https://www.nasdaq.com/symbol/'
      nasdaq_url = nasdaq_baseurl.__add__(nasdaq_symbol)

      #GET requesting nasdaq website for extraction of data
      url_fetch = c.get(nasdaq_url)
      soup = BeautifulSoup(url_fetch.text, 'html.parser')

      #Extracting Stock Name
      stock_variable_name = re.compile("var followObjTitle = \"(.*?)\";")
      stock_name = str(stock_variable_name.findall(soup.text))[2:-2]
      print("\nStock Name: ", stock_name)

      #Extracting Stock Price
      stock_price = soup.find('div',{'class':'qwidget-dollar'}).text
      print("Last Sale Price: ", stock_price)

      #Extracting Stock Netchange
      stock_netchange = soup.find('div',{'id':'qwidget_netchange'}).text

      #Checking whether the netchange trend is upward or downward
      determine_netchange_trend = soup.select('div[id="qwidget_netchange"]')[0]['class']
      downward_trend = "['qwidget-cents', 'qwidget-Red']"
      upward_trend = "['qwidget-cents', 'qwidget-Green']"


      if str(determine_netchange_trend) == downward_trend:
          print("Net Change: ", stock_netchange, "points Down")

      elif str(determine_netchange_trend) == upward_trend:
          print("Net Change: ", stock_netchange, "points Up")

      else:
          print("Net Change: N/A")
