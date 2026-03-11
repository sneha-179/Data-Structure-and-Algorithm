def anagram(s,t):
    if len(s)!=len(t):
        return False
    sd={}
    st={}
    for i in s:
        if i in sd:
            sd[i]+=1
        else:
            sd[i]=1
    for i in t:  
        if i in st:
            st[i]+=1
        else:
            st[i]=1
    print(sd)
    print(st)    
    return st==sd

print(anagram('aabcd','abcdd'))      

