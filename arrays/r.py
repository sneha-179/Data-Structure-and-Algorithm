k={}
nums=[2,3,3,3]
for num in nums:
    if num in k:
        k[num]+=1
    else:
        k[num]=1
print(k[2])    