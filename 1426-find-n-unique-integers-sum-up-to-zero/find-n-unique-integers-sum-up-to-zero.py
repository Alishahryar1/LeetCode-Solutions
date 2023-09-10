class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        output = [0] * n
        total = 0
        for i in range(1, n):
            output[i - 1] = i
            total += i
        output[-1] = -total
        return output
        