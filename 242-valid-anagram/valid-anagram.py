class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        def index(char):
            return ord(char) - ord('a')
       
        counts_s = [0] * 26
        counts_t = [0] * 26
        
        for i in range(len(s)):
            counts_s[index(s[i])] += 1
            counts_t[index(t[i])] += 1
        
        return counts_s == counts_t