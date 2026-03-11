class Solution():
    def backspaceCompare(self, s, t):
        stack_s=[]
        stack_t=[]
        for i in s:
            print(stack_s)
            if i!='#':
                stack_s.append(i)
            else:
                if stack_s:
                    stack_s.pop()
                
        for i in t:
            print(stack_t)
            if i!='#':
                stack_t.append(i)
            else:
                if stack_t:
                    stack_t.pop()
        print(stack_s,stack_t)
        return stack_t==stack_s
    
    #lc150
    def evalRPN(self, tokens):
        stack=[]
        for i in tokens:
            print(stack)
            if i in '+-/*':
                k=stack.pop()
                r=stack.pop()
                l=0
                if i=='+':
                    stack.append(k+r)
                elif i=='-':
                    stack.append(r-k)
                elif i=='*':
                    stack.append(k*r)
                else:
                    if (r/k)//1==0:
                        stack.append(r/k)
                    else:
                        if (r/k)>0:
                            stack.append(int(r/k)-1)
                        else:
                            stack.append(int(r/k)+1)                
            else:
                stack.append(int(i))    
        return stack[0]      

    #lc394
    def decodeString(self,s):
        stack=[]
        stri=''
        num=''
        def strr(t,i):
            if t[i]==']':
                return
            while ord(t[i])<58:
                num+=1
                i+=1
            stack.append([])    



k=Solution()
print(k.evalRPN(["3",'-4','+']))                
