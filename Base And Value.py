s=input()
s=s.lower()
s=list(s)
for i in s:
    if i.isdigit()==True:
        i=int(i)
    else:
        i=int(ord(i))-87

b=int(max(s))+1

s=s[::-1]
print('Base is ',b)
v=0
h=1
k=len(s)
for i in range(0,k):
    v=v+(int(s[i])*h)
    h*=b

print('Value is ',v)

