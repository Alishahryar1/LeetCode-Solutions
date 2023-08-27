class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = len(nums)
        i = 1
        s = 0
        while i < k:
            if nums[i - 1] == nums[i]:
                s += 1
            nums[i - s] = nums[i] 
            i += 1 
        return k - s