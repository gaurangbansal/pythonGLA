import time



n = int(input())
s = input()
q = int(input())
s1 = time.time()

for i in range(q):
    k = int(input())
    print(s.count(s[k-1],0,k-1))
f = time.time()

print(f-s1)
