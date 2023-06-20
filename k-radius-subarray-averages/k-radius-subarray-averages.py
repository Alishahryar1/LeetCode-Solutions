class Solution(object):
    def getAverages(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        left_sum = 0
        if k > len(nums) - 1:
            right_sum = sum(nums[1:])
        else:
            right_sum = sum(nums[1:k + 1])
        k_average = [0] * len(nums)
        for i, num in enumerate(nums):
            if i - k < 0 or i + k >= len(nums):
                k_average[i] = -1
            else:
                k_average[i] = (left_sum + num + right_sum)//(2*k + 1)
            if i - k >= 0:
                left_sum -= nums[i - k]
            left_sum += num
            if i + k + 1 < len(nums):
                right_sum += nums[i + k + 1]
            if i + 1 < len(nums):
                right_sum -= nums[i + 1]
        
        return k_average