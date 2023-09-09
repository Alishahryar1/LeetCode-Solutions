class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return max(nums)
        
        dp = [nums[0], max(nums[0], nums[1])]
        i = 2
        while i < len(nums):
            dp[0], dp[1] = dp[1], max(dp[1], dp[0] + nums[i])
            i += 1
        return dp[-1]