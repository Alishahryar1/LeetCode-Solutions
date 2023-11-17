class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        def distance(x, y):
            return x * x + y * y
    
        pts = [[distance(x, y), x, y] for x, y in points]
        heapq.heapify(pts)
        
        res = []
        for i in range(k):
            _, x, y = heapq.heappop(pts)
            res.append([x, y])
        
        return res