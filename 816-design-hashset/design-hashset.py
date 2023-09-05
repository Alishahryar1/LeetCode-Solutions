class MyHashSet(object):

    def __init__(self):
        self.size = 0
        self.capacity = 2
        self.hashSet = [None] * 2
    
    def hash(self, key):
        return key % self.capacity

    def rehash(self):
        oldSet = self.hashSet
        self.capacity *= 2
        self.hashSet = [None] * self.capacity
        self.size = 0
        for key in oldSet:
            if key != None:
                self.add(key)

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        index = self.hash(key)
        while True:
            if self.hashSet[index] in [None, -1]:
                self.hashSet[index] = key
                self.size += 1
                if self.size >= self.capacity // 2:
                    self.rehash()
                return
            elif self.hashSet[index] == key:
                return
            index += 1
            index = index % self.capacity
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        index = self.hash(key)
        while (self.hashSet[index] != None):
            if self.hashSet[index] == key:
                self.hashSet[index] = -1
                return
            index += 1
            index = index % self.capacity
        

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        index = self.hash(key)
        while (self.hashSet[index] != None):
            if self.hashSet[index] == key:
                return True
            index += 1
            index = index % self.capacity
        
        return False
        

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)