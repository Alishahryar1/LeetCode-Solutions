class object:
    def __init__(self, key = None, value = None):
        self.key = key
        self.value = value
        self.deleted = False

class MyHashMap(object):

    def __init__(self):
        self.capacity = 1000
        self.size = 0
        self.hashMap = [object() for _ in range(self.capacity)]

    def hash(self, key):
        return key % self.capacity

    def rehash(self):
        oldMap = self.hashMap
        self.capacity *= 2
        self.size = 0
        self.hashMap = [object() for _ in range(self.capacity)]
        for obj in oldMap:
            if not obj.deleted and obj.key != None:
                self.put(obj.key, obj.value)

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        index = self.hash(key)
        while True:
            obj = self.hashMap[index]
            if obj.key == None or obj.deleted:
                self.hashMap[index] = object(key, value)
                self.size += 1
                if self.size >= self.capacity // 2:
                    self.rehash()
                return
            elif not obj.deleted and obj.key == key:
                self.hashMap[index].value = value
                return
            index += 1
            index = index % self.capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        index = self.hash(key)
        while (self.hashMap[index].key != None):
            obj = self.hashMap[index]
            if not obj.deleted and obj.key == key :
                return obj.value
            index += 1
            index = index % self.capacity
        return -1

        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        index = self.hash(key)
        while (self.hashMap[index].key != None):
            obj = self.hashMap[index]
            if obj.key == key and not obj.deleted:
                obj.deleted = True
                return
            index += 1
            index = index % self.capacity
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)