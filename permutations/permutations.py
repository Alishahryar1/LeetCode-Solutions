class Solution(object):
    def helper(self, nums):
        if len(nums) == 1:
            return [nums]
        permutations = []
        for i in range(len(nums)):
            a = nums[:i]
            if i < len(nums) - 1:
                a += nums[i + 1:]
            current_perms = self.helper(a)
            for perm in current_perms:
                permutations.append([nums[i]] + perm)
        return permutations
    
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.helper(nums)