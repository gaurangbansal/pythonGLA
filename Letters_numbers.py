f=input('Enter a string : ')
m=len(f)
print ('Letters- ',m)
m=0
for i in f:
    if i.isdigit()==True:
        m+=1
print ('Numbers- ',m)
