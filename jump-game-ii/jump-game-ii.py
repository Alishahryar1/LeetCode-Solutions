class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            return 1
        
        i = len(nums) - 1
        step = 0
        while i > 0:
            min_i = i - 1
            j = i - 1
            while j >= 0:
                if nums[j] + j >= i:
                    if j < min_i:
                        min_i = j
                j -= 1
            i = min_i
            step += 1
        return step