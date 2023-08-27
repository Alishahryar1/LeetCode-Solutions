class MinStack(object):

    def __init__(self):
        self.stack = []
        self.mins = [float('inf')]

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if val <= self.mins[-1]:
            self.mins.append(val)
        self.stack.append(val)
        

    def pop(self):
        """
        :rtype: None
        """
        if self.mins[-1] == self.stack[-1]:
            self.mins.pop()
        return self.stack.pop()
         
        
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.mins[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()