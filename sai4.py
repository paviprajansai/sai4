n11=int(input())
l=list(map(int,input().split()))
for p in range(0,len(l)):
    max1=l[0]
for p in range(0,len(l)):
    if l[p]<max1:
        max1=l[p]
print(max1,end=" ")
for p in range(0,len(l)):
    min1=l[0]
for p in range(0,len(l)):
    if l[p]>min1:
        min1=l[p]
print(min1)
#i
