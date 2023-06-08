class Solution(object):
    def helper(self, n, matches):
        if n == 1:
            return matches

        if n % 2 == 0:
            matches += n // 2
            return self.helper(n//2, matches)
        else:
            matches += (n - 1)//2
            return self.helper((n - 1)//2 + 1, matches)
    
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        matches = 0
        return self.helper(n, matches)