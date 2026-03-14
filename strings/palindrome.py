def isPalindrome(s):
    s.lower()
    o=[]
    for a in s:
        if ord(a)>=97 and ord(a)<=122:
            o.append(a)
    return o==o[::-1] 

print(isPalindrome("A man, a plan, a canal: Panama"))     