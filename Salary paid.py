m=map(int,input().split())
m=list(m)
p=map(int,input().split())
p=list(p)
r=int(input())
s=map(int,input().split())
s=list(s)
t=0
for i in s:
    for j in range (0,len(m)-1):
        if i>=((m[j+1]-m[j])*p[j]*0.01):
            i-=(m[j+1]-m[j])*p[j]*0.01
        else:
            i=(i*100/p[j])+m[j]
            break
    if i>=0:
         i=(i*100/p[len(m)-1])+m[len(m)-1]
    t+=i+r
print (t)
