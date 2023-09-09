class Solution(object):
    def memoized_rob(self, n, nums, cache):
        if n in [len(nums) - 1, len(nums) - 2]:
            return nums[n]
        if n in cache:
            return cache[n]
        
        cache[n] = 0
        for i in range(n + 2, len(nums)):
            cache[n] = max(cache[n], self.memoized_rob(i, nums, cache))
        cache[n] += nums[n]
        return max(cache[n], self.memoized_rob(n + 1, nums, cache))
    
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return max(nums)
        
        return self.memoized_rob(0, nums, {})