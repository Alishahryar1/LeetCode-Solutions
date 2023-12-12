class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = b = 0
        for n in nums:
            if n > a:
                a, b  = n, a
            elif n > b:
                b = n
        return (a - 1) * (b - 1)