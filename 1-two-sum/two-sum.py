class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        presentMap = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in presentMap:
                return [i, presentMap[diff]]
            presentMap[num] = i