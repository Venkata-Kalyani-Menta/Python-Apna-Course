#Create a class called Order which stores item & its price. Use dunder function __gt__() greater than to convey that:
#order1 > order2 if price of order1 > price of order2

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, odr2):
        return self.price > odr2.price
    
odr1 = Order("chips", 20)
odr2 = Order("tea", 15)

print(odr1 > odr2) #true
            