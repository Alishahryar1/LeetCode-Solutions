class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L = R = 0
        while (R < len(nums)):
            count = 1
            while (R + 1 < len(nums) and nums[R] == nums[R + 1]):
                R += 1
                count += 1
            for i in range(min(count, 2)):
                nums[L] = nums[R]
                L += 1
            R += 1
        return L