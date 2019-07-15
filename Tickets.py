t=int(input())
for i in range(0,t):
    n=map(int,input().split())
    n=list(n)
    a=map(int,input().split())
    a=list(a)
    d=[0]
    for j in range(0, len(a)-1):
        m=0
        for k in range(j,len(a)):
            m+=a[k]
        for k in range(0,j+1):
            m+=d[k]
        m/=(len(a)-j)
        if (d[j]+a[j])>m:
            if (d[j] + a[j] -m) > n[1]:
                if a[j]>n[1]:
                    d.append(n[1])
                else:
                    d.append(a[j])
            elif a[j]<m:
                d.append(a[j])
            else:
                d.append(a[j]-m)
        else:
            d.append(0)
        a[j]-=d[j+1]


    for j in range(0,len(a)):
        a[j]+=d[j]
    a=map(int,a)
    a=list(a)
    print(max(as))
