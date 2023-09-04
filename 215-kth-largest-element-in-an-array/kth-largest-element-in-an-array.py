class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        for i, num in enumerate(nums):
            nums[i] = -num
        
        heapq.heapify(nums)
        for i in range(k):
            res = -heapq.heappop(nums)
        return res