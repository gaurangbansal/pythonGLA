def is_pangram(s):
    a='qwertyuiopasdfghjklzxcvbnm'
    s=s.lower()
    for i in a:
        if i in s:
            continue
        else:
            return False
    return True

s=input('Enter a string : ')
print (is_pangram(s))

    
