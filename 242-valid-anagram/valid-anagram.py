class Solution(object):
    def index(self, letter):
        return ord(letter) - 97
    
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
            counts_s[self.index(s[i])] += 1
            counts_t[self.index(t[i])] += 1
        
        for i in range(26):
            if counts_s[i] != counts_t[i]:
                return False
        
        return True