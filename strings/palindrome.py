def isPalindrome(s):
    n=''
    for i in s:
        if i.isalnum():
            n+=i.lower()
    return n==n[::-1]

print(isPalindrome('caracc'))     