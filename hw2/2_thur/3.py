lst=dict()
s=str(input())
for i in range(len(s)):
    if s[i] in lst.keys():
        lst[s[i]]+=1
    else:
        lst[s[i]]=1
        print(lst)
