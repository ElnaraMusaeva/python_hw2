s1=str(input())
s2=str(input())
c=0
for i in range(len(s1)):
    if s1[i] in s2:
        c+=1
if c==len(s1):
    print("True")
else:
    print("False")
