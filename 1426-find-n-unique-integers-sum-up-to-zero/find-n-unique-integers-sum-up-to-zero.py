class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        output = [0] * n
        for i in range(1, n):
            output[i - 1] = i
        
        output[-1] = -(n * (n - 1))//2
        return output
        