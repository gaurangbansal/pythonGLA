import math
x1, y1 =map(float,input('Enter coordinates for the first point : ').split())
x2, y2 =map(float,input('Enter coordinates for the second point : ').split())
d= math.sqrt((x1-x2)**2+(y1-y2)**2)
print ('Distance bwn the two points is %f.' %d)
