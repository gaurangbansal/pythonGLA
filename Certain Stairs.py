n=int(input())
m=[]
for i in range(0,n):
    if i== 0:
        m.append(1)
    elif i==1:
        m.append(2)
    elif i==2:
        m.append(4)
    else:
        m.append(m[i-3]+m[i-2]+m[i-1])



print (m[-1])
