def View(a):
    ma=0
    for i in a:
        m=a.count(i)
        if m>ma:
            ma=m
    return ma


a=map(int,input('Enter the radii of objects : ').split())
a=list(a)
print (View(a))
