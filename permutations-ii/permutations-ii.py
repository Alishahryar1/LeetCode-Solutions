class Solution(object):
    def helper(self, nums):
        
        if len(nums) == 1:
            return [nums]
        
        permutations = []
        
        for i in range(len(nums)):
            
            remaining_nums = nums[:i]
            
            if i < len(nums) - 1:
                remaining_nums += nums[i + 1:]
            
            perms = self.helper(remaining_nums)
            
            for perm in perms:
                new_perm = [nums[i]] + perm
                if new_perm not in permutations:
                    permutations.append(new_perm)
        
        return permutations
    
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.helper(nums)