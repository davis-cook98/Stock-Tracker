#Author: Davis Cook

#This will define the Stock class :
#A stock has a name which is a String
#A Symbol which is a String
#A Price which is a long
#More to come but this is the start

class Stock:
    #Defines the fields for a Stock
    def _init_(self, Name, Symbol, Price):
        self._Name = Name
        self._Symbol = Symbol
        self._Price = Price

    #Returns the stock's name
    def getName(self):
        return self._name

    #Returns the stock's symbol
    def getSymbol(self):
        return self._Symbol

    #Returns the stock's price
    def getPrice(self):
        return self._Price

    #Prints the stock's name followed by the price
    def Ticker(self):
        print(Name + "'s current price is: " + str(self._price))
