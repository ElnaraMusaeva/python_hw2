import random
n=int(input())
a=random.randint(1,100)
if n<a:
    print("more")
elif n>a:
    print("fewer")
elif n==a:
    print("BINGO!")