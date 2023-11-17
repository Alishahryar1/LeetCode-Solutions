class Solution(object):
    def distance(self, x, y):
        return x ** 2 + y ** 2
    
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        pts = [[self.distance(x, y), x, y] for x, y in points]
        heapq.heapify(pts)
        res = []
        for i in range(k):
            d, x, y = heapq.heappop(pts)
            res.append([x, y])
        return res