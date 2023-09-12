class Solution(object):
    def helper(self, text1, text2, i, j, cache):
        if i == len(text1) or j == len(text2):
            return 0
        key = (i, j)
        if key in cache:
            return cache[key]
        if text1[i] == text2[j]:
            cache[key] = 1 + self.helper(text1, text2, i + 1, j + 1, cache)
        else:
            cache[key] = max(self.helper(text1, text2, i, j + 1, cache), self.helper(text1, text2, i + 1, j, cache))
        return cache[key]
    
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        return self.helper(text1, text2, 0, 0, {})