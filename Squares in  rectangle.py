def square(a,b,c=0):
    if b>a:
        return square(b,a,c)
    elif a>b:
        return square(a-b,b,c+1)
    elif a==b:
        return c+1

a=int(input('Enter the length of rectangle : '))
b=int(input('Enter the breadth of rectangle : '))
c=square(a,b)
print ('The number of minimum squares is : ',c)
    
