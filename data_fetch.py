# Authors: Ajay Shah and Davis Cook

# Some imports for fetch data via http
from bs4 import BeautifulSoup
import requests
import re
from StockClass import Stock


def GetStock(symbol):
      nasdaq_baseurl = 'https://www.nasdaq.com/symbol/'
      nasdaq_url = nasdaq_baseurl.__add__(symbol)

      # Get requesting nasdaq website for extraction of data
      url_fetch = requests.get(nasdaq_url)
      soup = BeautifulSoup(url_fetch.text, 'html.parser')

      # Extracting Stock Name
      stock_variable_name = re.compile("var followObjTitle = \"(.*?)\";")
      stock_name = str(stock_variable_name.findall(soup.text))[2:-2]

      # Extracting Stock Price
      stock_price = soup.find('div',{'class':'qwidget-dollar'}).text

      # Making a "Stock" from the scraped data
      out = Stock(stock_name, symbol.upper(), stock_price)

      print(out)
      return(out)

# Test
# GetStock(input("What stock symbol?\n"))
