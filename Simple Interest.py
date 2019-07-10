p= float(input('Enter the principal amount : '))
r= float(input('Enter rate of interest : '))
t= float(input('Enter the time period (in years) : '))
a=(p*r*t)/100
print ('The interest on the basic amout is %f and the total amount is %f' %(a,a+p))
