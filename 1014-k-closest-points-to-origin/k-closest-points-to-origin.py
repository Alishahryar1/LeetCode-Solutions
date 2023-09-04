class Solution(object):
    def __init__(self):
        self.heap = [0]

    def distance(self, i):
        x, y = self.heap[i]
        return x ** 2 + y ** 2

    def percolate_down(self, i):
        while (2 * i < len(self.heap)):
            curr_dist = self.distance(i)
            left_dist = self.distance(2 * i)
            if 2 * i + 1 < len(self.heap) and self.distance(2 * i + 1) < left_dist and self.distance(2 * i + 1) < curr_dist:
                self.heap[i], self.heap[2 * i + 1] = self.heap[2 * i + 1], self.heap[i]
                i = 2 * i + 1
            elif left_dist < curr_dist:
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

    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        self.heapify(points)
        output = []
        for _ in range(k):
            output.append(self.pop())
        return output