m=input('Enter a list : ').split(',')
g=[]
for i in range (0,len(m)):
    if i%2==0:
        g.append(m[i])

l=','.join(g)
print (l)
