class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        counts = [0] * 3
        
        for num in nums:
            counts[num] += 1
        
        i = 0
        for n in [0,1,2]:
            for j in range(counts[n]):
                nums[i] = n
                i += 1
        return nums