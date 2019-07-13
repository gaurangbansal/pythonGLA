def unique(h):
    d=[]
    j=0
    for i in range (0,len(h)):
        m=0
        for l in range (0,j):
            if h[i]==d[l]:
                m=1
        if m==0:
            d.append(h[i])
            j+=1
    return d

f=map(int,input('Enter a list of repeated numbers : ').split())
a=list(f)
j=unique(a)
print ('The non repeated list is ',j)
