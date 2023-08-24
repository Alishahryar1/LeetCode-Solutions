class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        diff_present = {}
        for num in nums:
            diff_present[target - num] = -1
        for i, num in enumerate(nums):
            diff_present[num] = i
        for i, num in enumerate(nums):
            if diff_present[target - num] >= 0 and diff_present[target - num] != i:
                return [i, diff_present[target - num]]  