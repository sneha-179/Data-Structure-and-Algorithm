def compress(chars:list):
    if len(chars)==1 or len(chars)==0:
        return len(chars)
    i=0
    j=1
    count=1
    while j<len(chars):
        if chars[i]==chars[j]:
            print(count)
            count+=1
            if j==len(chars)-1 or chars[j+1]!=chars[i]:
                count=str(count)
                if int(count)>9:
                    chars[j]=count[0]
                    k=1
                    while k<len(count):
                        chars.insert(j+k,count[k])
                        k+=1

                else:
                    chars[j]=count[0]
                print(chars,j)              
                if j==len(chars)-len(count):
                    return(len(chars))
                i=j+1
                j+=2 
                count=1     
            else:
                chars.pop(j)
        else:
            i=j
            j+=1        
    return(len(chars))

print(compress(['a','a','a','b']))