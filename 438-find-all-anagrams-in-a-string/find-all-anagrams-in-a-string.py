class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(p) > len(s):
            return []
        def index(char):
            return ord(char) - ord('a')
        
        counts1 = [0] * 26
        counts2 = [0] * 26
        for i in range(len(p)):
            char = p[i]
            counts1[index(char)] += 1
            char = s[i]
            counts2[index(char)] += 1
        
        res = []
        for i in range(len(p), len(s)):
            if counts1 == counts2:
                res.append(i - len(p))
            char = s[i]
            counts2[index(char)] += 1
            char = s[i - len(p)]
            counts2[index(char)] -= 1

        if counts1 == counts2:
            res.append(i + 1 - len(p))  
        
        return res