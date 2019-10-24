a=list(map(int,input().rstrip().split()))
b=list(map(int,input().rstrip().split()))

x=int(input())

alice = 0
bob = 0
for i in range(x):
    if (a[i]>b[i]):
        alice+=1

    elif(a[i]<b[i]):
         bob+=1
print(alice)
