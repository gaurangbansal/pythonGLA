while 1:
    while 1:
        a=int(input('Choose any one \n1. For Celcius to Fahrenheit \n2. For Fahrenheit to celcius\n'))
        if a == 1:
            break
        elif a == 2:
            break
        else:
            print ('Wrong choice please try again')
    if a==1:
        c=float(input('Enter the temprature in Celcius : '))
        f=32+(1.8*c)
        print ('The tempratare in Fahrenheit is %d.' %f)
    if a==2:
        f=float(input('Enter the temprature in Fahrenheit : '))
        c=(5/9)*(f-32)
        print ('The tempratare in Celcius is %d.' %c)
    r=int(input('If you want to repeat type 1 '))
    if r==1:
        continue
    else:
        break
    
