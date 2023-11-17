class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        
        counts1 = [0] * 26
        counts2 = [0] * 26
        for i in range(len(s1)):
            char = s1[i]
            counts1[ord(char) - ord('a')] += 1
            char = s2[i]
            counts2[ord(char) - ord('a')] += 1
        
        if counts1 == counts2:
            return True
        
        for i in range(len(s1), len(s2)):
            char = s2[i]
            counts2[ord(char) - ord('a')] += 1
            char = s2[i - len(s1)]
            counts2[ord(char) - ord('a')] -= 1
            if counts1 == counts2:
                return True
        
        return False