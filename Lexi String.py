n=int(input())
for i in range(0,n):
    m=input()
    t=input()
    k=''
    for j in m:
        if j in t:
            k+=j
    print(k)
