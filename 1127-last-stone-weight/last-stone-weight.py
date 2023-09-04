class Solution(object):
    def __init__(self):
        self.heap = [0]

    def percolate_down(self, i):
        while (2 * i < len(self.heap)):
            if ((2 * i + 1 < len(self.heap)) and (self.heap[2 * i + 1] > self.heap[2 * i]) and (self.heap[2 * i + 1] > self.heap[i])):
                self.heap[i], self.heap[2 * i + 1] = self.heap[2 * i + 1], self.heap[i]
                i = 2 * i + 1
            elif self.heap[2 * i] > self.heap[i]:
                self.heap[i], self.heap[2 * i] = self.heap[2 * i], self.heap[i]
                i = 2 * i
            else:
                break

    def pop(self):
        if len(self.heap) == 2:
            return self.heap.pop()
        res = self.heap[1]
        self.heap[1] = self.heap.pop()
        self.percolate_down(1)
        return res
        
    def heapify(self, arr):
        arr.append(arr[0])
        self.heap = arr
        curr = (len(self.heap) - 1)//2
        while curr > 0:
            i = curr
            self.percolate_down(i)
            curr -= 1

    def push(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1
        while (i > 1 and self.heap[i // 2] < self.heap[i]):
            self.heap[i // 2], self.heap[i] = self.heap[i], self.heap[i // 2]
            i = i // 2
    
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        self.heapify(stones)
        while (len(self.heap) > 2):
            y = self.pop()
            x = self.pop()
            self.push(y - x)

        return self.heap[1]