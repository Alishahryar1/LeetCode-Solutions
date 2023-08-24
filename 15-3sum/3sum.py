class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        output = []
        for i in range(len(nums)):
            a = nums[i]
            if i > 0 and a == nums[i - 1]:
                continue
            L = i + 1
            R = len(nums) - 1
            while L < R:
                if L > i + 1 and nums[L] == nums[L - 1]:
                    L += 1
                    continue
                b = nums[L]
                c = nums[R]
                total = a + b + c
                if total == 0:
                    output.append([a, b, c])
                    L += 1
                    R -= 1
                elif total > 0:
                    R -= 1
                else:
                    L += 1
        
        return output