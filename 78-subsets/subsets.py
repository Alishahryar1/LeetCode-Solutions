class Solution(object):
    def helper(self, i, nums, stack, subsets):
        if i == len(nums):
            subsets.append(stack[:])
            return
        self.helper(i + 1, nums, stack, subsets)
        stack.append(nums[i])
        self.helper(i + 1, nums, stack, subsets)
        stack.pop()

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subsets = []
        self.helper(0, nums, [], subsets)
        return subsets