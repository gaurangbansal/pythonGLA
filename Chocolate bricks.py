def make_chocolate(a,b,c):
    s=0
    for i in range(1,b+1):
        s+=5
        if s>c:
            s-=5
            break
    i-=1
    for j in range (1,a+1):
        s+=1
        if s==c:
            return j
    return -1


a=int(input('Enter the number of 1 kg boxes available : '))
b=int(input('Enter the number of 5 kgs boxes available : '))
c=int(input('Enter the amount of chocolate required : '))
l=make_chocolate(a,b,c)
if l==-1:
    print('Not available, sorry.')
else:
    print ('The number of 1 kg boxes used are ',l)
