def func(a,b):
    if a>2*b:
        return 1
    else:
        f=a        
    return f*func(a+1,b)
n=int(input())
sum=0
for i in range(1,n+1):
    b=i
    sum+=func(i,b)
print(sum)
