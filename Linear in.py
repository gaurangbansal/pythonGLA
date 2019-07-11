def linearin(a,b):
    l=0
    for i in range(0,len(a)):
        if l==len(b):
            return True
        else:
            if a[i]==b[l]:
                l+=1
            elif a[i]>b[l]:
                break
    return False

l= map(int,input('Enter the outer list : ').split())
m=list(l)
k=map(int,input('Enter the inner list : ').split())
n=list(k)
s=linearin(m,n)
print (s)
