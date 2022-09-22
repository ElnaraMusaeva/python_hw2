n=int(input())
a=n//100
b=(n%100)//10
c=n%10
if a<b and b<c:
 print("yes")
else:
    print("no")