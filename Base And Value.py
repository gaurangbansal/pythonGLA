s=input()
s=s.lower()
s=list(s)
for i in range(0,len(s)):
    if s[i].isdigit()==True:
        s[i]=int(s[i])
    else:
        s[i]=int(ord(s[i]))-87

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

