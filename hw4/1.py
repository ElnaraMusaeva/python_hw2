class Investment():
    def __init__(self,principal, interset):
        self.principal=principal
        self.interset=interset
    def value_after(self,n):
        return self.principal*(1+((self.interset/100)*n))
    def __str__(self):
        return f'Principal-${self.principal}, Interset rate - {self.interset}'
stavka=int(input("stavka: "))
summa=int(input("summa: "))
s=Investment(summa,stavka)
print(s)
n=int(input())
print(s.value_after(n))
