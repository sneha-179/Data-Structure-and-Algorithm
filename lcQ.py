from collections import deque
class Solution(object):
    def strStr(self,haystack,needle):
        i=0
        index=deque()
        n=len(needle)
        while i<=len(haystack)-n:
            k=0
            found=0
            while k<n:
                if haystack[i+k]==needle[k]:
                    if haystack[i+k]==needle[0] and k!=0:
                        index.append(k)
                    found+=1
                else:
                    break
                print("*")
                k+=1
            if found==n:
                return i
            if not index:
                i=i+k+1
            else:
                i=index[0]
                index.popleft()
        return -1

k=Solution()
print(k.strStr('"mississippi"','issipi'))                    