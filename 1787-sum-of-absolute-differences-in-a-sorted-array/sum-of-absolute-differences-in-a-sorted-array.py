class Solution(object):
    def getSumAbsoluteDifferences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        left_sum, right_sum, res = 0, sum(nums), [0] * n
        for i in range(n):
            right_sum -= nums[i]
            nums_to_left, nums_to_right = i, n - 1 - i
            res[i] = (nums_to_left * nums[i]) - left_sum + right_sum - (nums_to_right * nums[i])
            left_sum += nums[i]

        return res