import math
##print(dir(math))

a=float(input('Enter value of a : '))

h=float(input('Enter value of h : '))
SA=6*a*h*(a+h)
V=1.5*math.sqrt(3)*(a**2)*h

print('The surface area is %f.\nThe volume is %f.'%(SA,V))
