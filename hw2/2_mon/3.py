s1=str(input())
s2=s1.lower()
for i in range(len(s2)):
    if s2[i]!=" ":
        print(ord(s2[i])-96, end=" ")
