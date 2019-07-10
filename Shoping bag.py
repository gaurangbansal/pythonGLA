h=list()
while 1:
    h.append(input('Enter item for shopping bag :'))
    if h[-1]==' ' or h[-1]=='':
        del h[-1]
        break
print (h)
