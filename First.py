a=open('abc.txt','r')
l=a.read().split('\n')
print(len(l))
a.seek(0,0)
n=a.read().split()
print (len(n))
a.seek(0,0)
z=a.read()
print(len(z))
