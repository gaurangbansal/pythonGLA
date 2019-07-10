a,b,c=map(int, input('Enter any three numbers: ').split())
m=a
if b>a:
    if c>b:
        m=c
    else:
        m=b
elif c>a:
    m=c
print ('Among %d %d %d, %d is the largest.'%(a,b,c,m))

