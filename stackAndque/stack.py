#leetcode155
class MinStack(object):
    def __init__(self):
        self.stack=[]

    def push(self,val):
        self.stack.append(val)
    def pop(self):
        if self.isEmpty() :
            return 'Stack is empty'
        k=self.stack.pop()    
        return k
    
    def top(self):
        if self.isEmpty():
            return 'Stack is empty'
        return self.stack[-1]
    
    def getMin(self):
        if self.isEmpty():
            return 'Stack is empty'
        return min(self.stack)
    
    def isEmpty(self):
        if len(self.stack)==0:
            return True
        
k=MinStack()
print(k.pop())
print(k.push(1))
print(k.push(2))
print(k.pop())
print(k.top())
print(k.push(0))
print(k.getMin())        


