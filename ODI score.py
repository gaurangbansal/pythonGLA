

def swap(a):
    a[0]=a[0]+a[1]
    a[1]=a[0]-a[1]
    a[0]=a[0]-a[1]
    return a

rr1=float(input())
a=map(int,input().split())
a=list (a)
p=input().split()
p=list(p)
b=len(p)
r=0
for i in p:
    if i.isdigit()==True:
        r+=int(i)
rr2=float(input())
x=float((rr2*(b/6)-r)/(rr1-rr2))
t=rr1*x + r

for i in  range(0,b):
    if p[i]=='W' or p[i]=='w':
        a[0]=0
    elif int(p[i])%2==0:
        a[0]+=int(p[i])
    else :
        a[0]+=int(p[i])
        a=swap(a)
    if i%6==3:
        a=swap(a)


print('%d %d %d'%(t,a[0],a[1]))
