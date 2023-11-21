class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        L, total, minLength = 0, 0, len(nums) + 1
        for R in range(len(nums)):
            total += nums[R]
            while total >= target:
                minLength = min(R - L + 1, minLength)
                total -= nums[L]
                L += 1
        
        return 0 if minLength == len(nums) + 1 else minLength