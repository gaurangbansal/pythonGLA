def issorted(h):
    s=h[:]
    s.sort()
    if s == h:
        return True
    else:

        return False

print(issorted([2,4,5,7]))    

