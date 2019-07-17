t=int(input())
d=float(input())
h=t*d/360
m=h-int(h)
h=int(h)
m*=60


h=h*30+m*0.5
m*=6

if h>m:
    a=h-m
else:
    a=m-h



print(a)
