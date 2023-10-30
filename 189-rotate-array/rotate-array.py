class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        temp = nums[len(nums) - k:]
        i = len(nums) - k - 1
        while (i >= 0):
            nums[i + k] = nums[i]
            i -= 1
        for i in range(k):
            nums[i] = temp[i]