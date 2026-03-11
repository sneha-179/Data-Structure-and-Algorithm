class Solution(object):
    def longestCommonPrefix(self,strs):
        if len(strs)==1:
            return strs[0]
        final_index=len(strs[0])
        j=1
        while j<len(strs):
            k=0
            while k<min(len(strs[0]),len(strs[j])):
                if k>final_index-1:
                    break
                if strs[0][k]==strs[j][k]:
                    k+=1
                else:
                    break
            if k<final_index:
                final_index=k        
            j+=1
        if final_index<0:
            return ''
        return str(strs[1][0:final_index]) 

k=Solution()       
print(k.longestCommonPrefix([""]))    
