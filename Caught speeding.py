def caught_speeding(a, b):
    if b=='True':
        if a<=65:
            return 0
        elif a in range(66,86):
            return 1
        else:
            return 2
    elif b=='False':
        if a<=61:
            return 0
        elif a in range(61,81):
            return 1
        else:
            return 2
    else:
        return 3

s=str(input('Is it your birthday (True\False) : '))
n=int(input('Enter your vehicle speed : '))
c=caught_speeding(n,s)
if c==0:
    print ('No ticket')
elif c==1:
    print ('Small ticket')
elif c==2:
    print ('Big ticket')
else:
    print ('Wrong inputs')
