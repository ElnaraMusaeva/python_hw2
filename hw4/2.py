class Product:
    def __init__(self, n price):
        self.n=n
        self.price=price   
    def get_price(self, m):
        if m<10:
            return self.price
        elif m>=10 and m<99:
            return 0.9*self.price
        elif m>100
            return 0.8*self.price
    def make_purchase(self,l):
        if l<self.n:
            self.n-=l
            return self.get_price(l)*l
        else:
            return 0
    total_amount=0
    apple=Product(20, 250)
    lemon=Product(27, 600)
    orange=Product(120, 1050)
    total_amount=apple.make_purchase(15)+lemon.make_purchase(5)+orange.make_purchase(20)
    print(total_number)
