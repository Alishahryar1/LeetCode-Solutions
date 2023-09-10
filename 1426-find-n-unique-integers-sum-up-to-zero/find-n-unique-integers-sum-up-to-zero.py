class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        output = [i for i in range(1, n)]
        output.append(-(n * (n - 1))//2)
        return output
        