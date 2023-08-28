class object():
    def __init__(self, url = "", prev = None, next = None):
        self.url = url
        self.prev = prev
        self.next = next

class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.head = object(homepage)
        self.curr = self.head
        
    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        self.curr.next = object(url, self.curr)
        self.curr = self.curr.next
        

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        for i in range(steps):
            if self.curr.prev == None:
                break
            self.curr = self.curr.prev
        return self.curr.url
        

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        for i in range(steps):
            if self.curr.next == None:
                break
            self.curr = self.curr.next
        return self.curr.url
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)