class Solution(object):
    #Q53
    def maxSubArray(self,nums):
        if len(nums)==1:
            return nums[0]
        i=0
        j=1
        k=1
        res=nums[0]
        sum=nums[0]
        sum2=nums[0]
        while j<len(nums) and i<len(nums) and k<len(nums):
            sum+=nums[j]
            if (sum2+nums[k])<=(nums[k]):
                sum-=sum2
                i=k
                sum2=nums[i]
            else:    
                sum2+=nums[k] 
            print(sum2,nums[k])           
            k+=1    
            j+=1  
            res=max(sum,res)
        return res
    
    #lc121
    def maxProfit(self,prices):
        max_p=0
        while j<len(prices) and i<j:
            max_p=max(prices[j]-prices[i],max_p)
            if prices[j]-prices[i]<0:
                i=j
            j+=1
        if max_p<0:
            return 0    
        return max_p    
    
    #lc26
    def removeDuplicates(self,nums):
        last_unique=-101
        replace=0
        for i in range(len(nums)):
            print(last_unique,replace,sep=' ')
            if nums[i]>last_unique:
                last_unique=nums[i]
                print(nums[replace])
                nums[i]=nums[replace]
                nums[replace]=last_unique
                replace+=1
                print(nums)
        return replace     

    #lc27
    def removeElement(self,nums,val):
        if len(nums)==0:
            return 0
        i=0
        j=len(nums)-1 
        k=0 
        while i<=j:
            if nums[i]==val:
                if nums[j]!=val:
                    nums[i],nums[j]=nums[j],nums[i]
                    k+=1
                    i+=1
                j-=1
            else:
                k+=1
                i+=1        
            print(nums,i,j,sep=' ')    
        print(nums,i,j,sep=' ')    
        return k

    #lc344
    def reverseString(self,s):
        s=s[::-1]
        return s
    
    #lc283
    def moveZeroes(self, nums):
        i=0
        j=1
        while j<len(nums) and i<len(nums):
            print(nums,i,j,sep=' ')
            if nums[i]==0:
                while j<len(nums) and nums[j]==0:
                    j+=1
                if j<len(nums) and nums[j]!=0:
                    nums[i],nums[j]=nums[j],nums[i]
            else:
                j+=1        
            i+=1
        return nums  

    #lc20
    def isValid(self,s):
        leftBrac=['(','{','[']
        rightBrac=[')','}',']']
        stack=[]
        for i in s:
            print(stack)
            if i in leftBrac:
                stack.append(i)
            else:
                if len(stack)>0 and leftBrac.index(stack[-1])==rightBrac.index(i):
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True  

    def removeElement(self,nums,val):
        if len(nums)==0:
            return 0
        i=0
        j=len(nums)-1
        while i!=j and i<len(nums) and j>0:
            if nums[i]==val:
                while nums[j]==val and i<j:
                    j-=1
                nums[i],nums[j]=nums[j],nums[i]
                if i==j:
                    break
                j-=1
            print(nums,i,j,sep=' ')  
            if i!=j:
                i+=1 
        if nums[i]==val:
            return i
        return i+1  

    def majorityElement(self,nums):
        freq={}
        val=int(len(nums)/2)
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1    
            if freq[num]>val:
                return num

    def maxProfit(self, prices):
        k=prices[0]
        maxprofit=0
        for price in prices:
            if (price-k)<0:
                k=price
            maxprofit=max(maxprofit,price-k)
        return maxprofit        






k=Solution()
print(k.maxProfit([7,6,4,3,2,1,5]))
