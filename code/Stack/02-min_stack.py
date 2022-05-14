# EASY
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val):
        self.stack.append(val)
        minVal = min(val,self.minStack[-1] if self.minStack else val)
        self.minStack.append(minVal)
        
    def pop(self):
        self.stack.pop()
        self.minStack.pop()

    def top(self):
        return self.stack[-1]
        

    def getMin(self):
        return self.minStack[-1]


obj = MinStack()

obj.push(5)
obj.push(10)
obj.push(7)
obj.push(2)
obj.push(7)
obj.push(18)
obj.pop()

obj.getMin()
