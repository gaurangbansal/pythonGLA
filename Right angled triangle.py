a,b,c=map(int, input('Enter three sides of triangle: ').split())
m=0
if a**2==b**2+c**2:
    m=1
if c**2==b**2+a**2:
    m=1
if b**2==a**2+c**2:
    m=1
if m==1:
    print ('The triangle is right angled triangle.')
else:
    print ('The triangle is not a right angled triangle.')
