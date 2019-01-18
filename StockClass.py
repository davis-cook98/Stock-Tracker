#Author: Davis Cook

#This will define the Stock class :
#A stock has a name which is a String
#A Symbol which is a String
#A Price which is a long

class Stock:
    def __init__(self, Name, Symbol, Price):
        self.Name = Name
        self.Symbol = Symbol
        self.Price = Price


X = Stock("Apple", "AAPL", 203.77)

print(X.Name)
print(X.Symbol)
print(X.Price)
