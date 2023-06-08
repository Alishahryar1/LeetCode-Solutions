class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        target_indices = []
        nums.sort()
        for i, num in enumerate(nums):
            if num == target:
                target_indices.append(i)
        return target_indices