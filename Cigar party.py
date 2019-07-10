def cigar_party(a, b):
    if b=='True':
        if a>=40:
            return 1
        else:
            return 0
    elif b=='False':
        if a in range(40,61):
            return 1
        else:
            return 0
    else:
        return 2

s=str(input('Is it weekend (True\False) : '))
n=int(input('Enter the number of cigars : '))
c=cigar_party(n,s)
if c==1:
    print ('Party is ON')
elif c==0:
    print ('No party today')
else:
    print ('Wrong inputs')
