def fac(n,p=1):
    if n==0:
        return p
    else:
        p*=n
        return fac(n-1,p)
def c(n,m):
    
    return fac(n)/(fac(m)*fac(n-m))

n=int(input())

for i in range(0,n):
    t=map(int,input().split())
    t=list(t)
    N=t[0]
    T=t[1]
    M=t[2]
    
    nu=c(N,M)
    d=nu-c(N-T,M)
    


    print(float(d/nu))


## logic by Mr. Sagar Singhal
