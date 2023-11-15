class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        L, R = 0, n - 1
        res = float('inf')
        while (L <= R):
            if nums[L] < nums[R]:
                return min(res, nums[L])
            m = (L + R)//2
            res = min(res, nums[m])
            if nums[m] >= nums[L]:
                L = m + 1
            else:
                R = m - 1
        return res