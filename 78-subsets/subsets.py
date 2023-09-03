class Solution(object):

    def helper(self, nums, output):
        if len(nums) == 0:
            return 
        if nums not in output:
            output.append(nums)
        for i in range(len(nums)):
            new_nums = []
            for j in range(len(nums)):
                if i == j:
                    continue
                new_nums.append(nums[j])
            self.helper(new_nums, output)

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = [[]]
        self.helper(nums, output)
        return output