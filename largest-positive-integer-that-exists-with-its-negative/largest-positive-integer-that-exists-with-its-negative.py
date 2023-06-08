class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = -1
        for num in nums:
            abs_num = abs(num)
            if abs_num > max_num:
                if -num in nums:
                    max_num = abs_num
        return max_num