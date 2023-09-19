class Solution(object):
    def canPartition(self, nums):
        target = sum(nums)
        if target % 2 != 0:
            return False
        else:
            target //= 2
        prevRow = [False] * (target + 1)
        prevRow[0] = True
        for num in nums:
            newRow = [False] * (target + 1)
            for j in range(target + 1):
                if prevRow[j] or j - num >= 0 and prevRow[j - num]:
                    newRow[j] = True
            prevRow = newRow
        return prevRow[-1]