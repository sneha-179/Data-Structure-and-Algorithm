class Solution(object):
    #lc349
    def intersection(self,nums1,nums2):
        output=[]
        nums1=set(nums1)
        nums2
        for n in set(nums1):
            if n in set(nums2):
                output.append(n)
        return output    

    #lc350   
    def intersect(self,nums1,nums2):
        res=[]
        h1={}
        h2={}
        for n in nums1:
            if n in h1:
                h1[n]+=1
            else:
                h1[n]=1    
        for n in nums2:
            if n in h2:
                h2[n]+=1
            else:
                h2[n]=1    
        for n in h1:
            if n in h2:
                k=min(h1[n],h2[n])
                i=1
                while i<=k:
                    res.append(n)
                    i+=1
        return res    

    #lc202
    def isHappy(self,n):
        if n<10:
            if n==1 or n==7:
                return True
            else:
                return False
        sum=0
        while sum!=1:
            k=str(n)
            for i in k:
                sum+=(int(i)**2)
            if sum<10 and sum!=7 and sum!=1:
                return False
            if sum==1 or sum==7:
                return True
            print(sum)     
            n=sum
            sum=0    
                
                
k=Solution()
print(k.isHappy(4))        
