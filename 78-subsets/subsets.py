class Solution(object):

    def helper(self, nums, output, i, subset):
        if i == len(nums):
            output.append(subset)
            return
        self.helper(nums, output, i + 1, subset + [nums[i]])
        self.helper(nums, output, i + 1, subset)

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = []
        self.helper(nums, output, 0, [])
        return output