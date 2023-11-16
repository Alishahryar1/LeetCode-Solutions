class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        L = R = 0
        chars = {}
        maxlen = 0
        while R < len(s):
            if s[R] in chars:
                i = chars[s[R]]
                while L <= i:
                    del chars[s[L]]
                    L += 1
                chars[s[R]] = R
                R += 1
                continue
            chars[s[R]] = R
            maxlen = max(maxlen, R - L + 1)
            R += 1
        
        return maxlen