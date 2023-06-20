class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        counts = {}
        for letter in s:
            counts[letter] = 0
        for letter in s:
            counts[letter] += 1
        len_max = 0
        odd = False
        for letter in counts.keys():
            if counts[letter] % 2 == 0:
                len_max += counts[letter]
            else:
                len_max += counts[letter] - 1
                odd = True
        
        if odd:
            len_max += 1
        
        return len_max