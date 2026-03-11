class Solution(object):
    def twoSum(self,nums,target):
        num={}
        for i in range(len(nums)):
            if nums[i] in num:
                num[nums[i]][0]+=1
                num[nums[i]].append(i)
            else:
                num[nums[i]]=[1,i]  
        for i in range(len(nums)):
            num[nums[i]][0]-=1
            if target-nums[i] in num and num[target-nums[i]][0]!=0:
                return [i,num[target-nums[i]][len(num[target-nums[i]])-1]]

k=Solution()
print(k.twoSum([3,3],6))            

                


