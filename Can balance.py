def canbalance(*h):
    sm=0
    for i in h:
        sm+=i
    s=0
    sm/=2
    for j in h:
        s+=j
        if s==sm:
            return True
        elif s>sm:
            return False


h=map(int,input('Enter a array to be balance : ').split(' '))
d=canbalance(*h)
print(d)
