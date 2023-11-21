class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        L, R, chars, maxlen = 0,0,{},0
        while R < len(s):
            while (s[R] in chars):
                del chars[s[L]]
                L += 1

            chars[s[R]] = R
            maxlen = max(maxlen, R - L + 1)
            R += 1
        
        return maxlen