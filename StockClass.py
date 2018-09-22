#This will define the Stock class :
#A stock has a name which is a String
#A Symbol which is a String
#A Price which is a long
#More to come but this is the start

class Stock:
    def _init_(self, Name, Symbol, Price):
        self._Name = Name
        self._Symbol = Symbol
        self._Price = Price

    def getName(self):
        return self._name

    def getSymbol(self):
        return self._Symbol

    def getPrice(self):
        return self._Price

    def Ticker(self):
        print(Name + "'s current price is: " + str(self._price))
