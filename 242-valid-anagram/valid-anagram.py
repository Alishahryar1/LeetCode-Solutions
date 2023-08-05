class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        counts_s = [0] * 26
        counts_t = [0] * 26
        
        for i in range(len(s)):
            counts_s[ord(s[i]) - 97] += 1
            counts_t[ord(t[i]) - 97] += 1
        
        return counts_s == counts_t