class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for i, num in enumerate(nums):
            j = (i + 1) % len(nums)
            next_greater = -1
            while j != i:
                if nums[j] > nums[i]:
                    next_greater = nums[j]
                    break
                j += 1
                j = j % len(nums)
            ans.append(next_greater)
        return ans