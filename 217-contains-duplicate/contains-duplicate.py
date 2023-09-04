class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        presentMap = {}
        for num in nums:
            if num not in presentMap:
                presentMap[num] = 1
            else:
                presentMap[num] += 1
            if presentMap[num] >= 2:
                return True
        
        return False