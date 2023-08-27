class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = len(nums)
        i = 0
        s = 0
        while i < k:
            nums[i - s] = nums[i]
            if nums[i] == val:
                s += 1
            i += 1
        return k - s