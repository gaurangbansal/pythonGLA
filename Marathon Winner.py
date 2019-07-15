n=int(input())
t=int(input())
d=[]
for i in range(0,n):
    a=map(int,input().split())
    a=list()
    a.append(0)
    d.append(a)

for j in range(0,t-1,2):
    ma=0
    q=0
    for k in range(0,n):
        m=(d[k][j]+d[k][j+1])*d[k][t]
        if m>ma:
            q=k
    d[q][t+1]+=1

l=0
for x in range(0,n):
    if d[x][t+1]>l:
        p=x


print(p+1)
