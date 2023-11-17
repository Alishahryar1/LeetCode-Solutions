class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        L, R = 0, len(numbers) - 1
        while L < R:
            s = numbers[L] + numbers[R]
            if target > s:
                L += 1
            elif target < s:
                R -= 1
            else:
                return [L + 1, R + 1]