class MyStack(object):

    def __init__(self):
        self.queue = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue.append(x)

        

    def pop(self):
        """
        :rtype: int
        """
        queue2 = []
        for i in range(len(self.queue) - 1):
            queue2.append(self.queue.pop(0))
        a = self.queue.pop(0)
        self.queue = queue2
        
        return a
        

    def top(self):
        """
        :rtype: int
        """
        queue2 = []
        for i in range(len(self.queue) - 1):
            queue2.append(self.queue.pop(0))
        a = self.queue[0]
        queue2.append(a)
        self.queue = queue2
        return a

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.queue) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()