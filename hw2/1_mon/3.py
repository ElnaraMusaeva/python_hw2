def sum(a,b,c):
    d=a**3+b**3+c**3
    return d
for i in range(100,1000):
    a=int(i/100)
    b=int(i/10)%10
    c=i%10
    s=str(a)+str(b)+str(c)
    if int(s)==sum(a,b,c):
        print(int(s))
