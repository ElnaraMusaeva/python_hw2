a,b,c,d,e,f=map(int, input().split())
count=0
if a%2==1:
    count+=1
elif b%2==1:
    count+=1
elif c%2==1:
    count+=1
elif d%2==1:
    count+=1
elif e%2==1:
    count+=1
elif f%2==1:
    count+=1
else:
    print("No")
print(count)