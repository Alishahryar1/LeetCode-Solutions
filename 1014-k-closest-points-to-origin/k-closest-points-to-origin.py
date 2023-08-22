class Solution(object):
    def sort_key(self, point):
        x, y = point
        return x**2 + y**2
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        points.sort(key = self.sort_key)
        return points[:k]