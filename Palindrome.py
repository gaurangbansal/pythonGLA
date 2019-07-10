s=str(input('Enter a string to be checked for palindrome : '))
def reverse(s):
    return s[::-1]
def ispalindrome(s):
    t=reverse(s)
    if t==s:
        return 1
    else:
        return 0
a=ispalindrome(s)
if a==1:
    print ('%s is a palindrome' %s)
else:
    print ('%s is not a palindrome' %s)
