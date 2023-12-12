class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = 0
        heap = []
        for n in nums:
            if len(heap) < 2:
                heapq.heappush(heap, n)
            elif heap[0] < n:
                heapq.heappushpop(heap, n)
        return (heap[0] - 1) * (heap[1] - 1)