class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        reachable = [False] * len(nums)
        reachable[-1] = True
        i = len(nums) - 2
        j = len(nums) - 1
        while i >= 0:
            if i + nums[i] >= j:
                reachable[i] = True
                j = i
            i -= 1
        return reachable[0]