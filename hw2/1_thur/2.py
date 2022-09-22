from this import d


n=int(input())
a=n//10000
b=n%10000//1000
c=n%1000//100
d=n%100//10
e=n%10
print(a*10000+b*2000+c*100+d*20+e)