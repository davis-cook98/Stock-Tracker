#Author: Davis Cook

#This will define the Stock class :
#A stock has a name which is a String
#A Symbol which is a String
#A Price which is a long

class Stock:
    #Defines the fields for a Stock
    def __init__(self, Name, Symbol, Price, nChange):
        self.name = Name
        self.symbol = Symbol
        self.price = Price
        self.change = nChange

    def __str__(self):
        return ', '.join(['{key}={value}'.format(key=key, value=self.__dict__.get(key)) for key in self.__dict__]

X = Stock(Name="Apple", Symbol="AAPL", Price=203.77 nChange=1.03)

print(X)
