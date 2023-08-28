class object():
    def __init__(self, val = 0, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

        
    def getNode(self, index):
        curr = self.head
        for i in range(index):
            curr = curr.next
        return curr        

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index >= 0 and index < self.length:
            return self.getNode(index).val
        else:
            return -1

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        if self.length == 0:
            self.head = object(val)
            self.tail = self.head
        else:
            temp = object(val, self.head)
            self.head.prev = temp
            self.head = temp
        self.length += 1
        

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        if self.length == 0:
            self.tail = object(val)
            self.head = self.tail
        else:
            temp = object(val, prev = self.tail)
            self.tail.next = temp
            self.tail = temp
        self.length += 1

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index > self.length:
            return  
        if index <= 0:
            self.addAtHead(val)
            self.length -= 1
        elif index == self.length:
            self.addAtTail(val)
            self.length -= 1
        else:
            prev = self.getNode(index - 1)
            temp = object(val, prev.next, prev)
            prev.next.prev = temp
            prev.next = temp
        self.length += 1
        

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.length:
            return
        if self.length == 1:
            self.head = None
            self.tail = None
        elif index == 0:
            self.head = self.head.next
            self.head.prev = None
        elif index == self.length - 1:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            prev = self.getNode(index - 1)
            latter = prev.next.next
            prev.next = latter
            latter.prev = prev
        self.length -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)