class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.heap = [float('-inf')]
        self.k = k
        for num in nums:
            self.add(num)
        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.heap) < self.k + 1:
            self.heap.append(val)
            i  = len(self.heap) - 1
            while self.heap[i // 2] > self.heap[i]:
                self.heap[i // 2], self.heap[i] = self.heap[i], self.heap[i // 2]
                i /= 2
            return self.heap[1]
        
        if val > self.heap[1]: 
            if len(self.heap) == 1:
                return None
            if len(self.heap) == 2:
                self.heap[1] = val
            else:
                self.heap[1] = self.heap.pop()
                i = 1
                while 2 * i < len(self.heap):
                    if (2 * i + 1 < len(self.heap) and 
                    self.heap[2 * i + 1] < self.heap[2 * i] and 
                    self.heap[i] > self.heap[2 * i + 1]):
                        # Swap right child
                        tmp = self.heap[i]
                        self.heap[i] = self.heap[2 * i + 1]
                        self.heap[2 * i + 1] = tmp
                        i = 2 * i + 1
                    elif self.heap[i] > self.heap[2 * i]:
                        # Swap left child
                        tmp = self.heap[i]
                        self.heap[i] = self.heap[2 * i]
                        self.heap[2 * i] = tmp
                        i = 2 * i
                    else:
                        break
                self.add(val)
                    
        return self.heap[1]

            

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)