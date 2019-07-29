a=int(input())
b=list(map(int,input().split()))
l=[]
l1=[]
for i in b:
    if i not in l:
        l.append(i)
    else:
        l1.append(i)
for i in l:
    if i not in l1:
        print(i)
