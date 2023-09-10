class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        output = []
        total = 0
        for i in range(1, n):
            output.append(i)
            total += i
        output.append(-total)
        return output
        