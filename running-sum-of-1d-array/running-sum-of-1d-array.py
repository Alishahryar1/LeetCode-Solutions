class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        running_sum = 0
        L = [0] * len(nums)
        for i, num in enumerate(nums):
            running_sum += num
            L[i] = running_sum
        return L