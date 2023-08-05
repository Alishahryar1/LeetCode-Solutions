class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        present = {}
        for num in nums:
            present[num] = False
        for num in nums:
            if not present[num]:
                present[num] = True
            else:
                return True
        return False