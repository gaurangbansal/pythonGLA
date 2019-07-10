a=int(input('Enter a number : '))
b=0
for i in range (2,int(a/2)):
    if a%i==0:
        b=1
        break
if b==0:
    print ('%d is a pr
