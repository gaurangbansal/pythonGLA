def mod (x):
    if x<0:
        return -x
    else:
        return x


n=int(input())
m=[]
for i in range (0,n):
    k=map(int,input().split())
    k=list(k)
    m.append(k)


o=map(int,input().split())
o=list(o)

s=[]
for j in range(1,n+1):
    x=mod(m[j-1][0]-o[0])
    y=mod(m[j-1][1]-o[1])

    if mod(m[j-1][2]-o[0])<x:
        x=mod(m[j-1][2]-o[0])
    if mod(m[j-1][3]-o[1])<y:
        y=mod(m[j-1][3]-o[1])

    d=[x+y,j]
    s.append(d)

s=sorted(s)
#print(s)
j=[]
for i in range(0,n):
    j.append(str(s[i][1]))
    
l=' '.join(j)
print(l)
