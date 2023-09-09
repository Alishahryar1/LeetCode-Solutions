class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return max(nums)
        
        a, b = nums[0], max(nums[:2])
        for i in range(2, len(nums)):
            a, b = b, max(a + nums[i], b)
        return b