class Solution(object):
    def reverse(self, L, R, arr):
        while (L < R):
            arr[L], arr[R] = arr[R], arr[L]
            L += 1
            R -= 1
    
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        self.reverse(0, len(nums) - 1, nums)
        self.reverse(0, k - 1, nums)
        self.reverse(k, len(nums) - 1, nums)
        