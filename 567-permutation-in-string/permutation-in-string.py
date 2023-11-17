class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False

        def index(char):
            return ord(char) - ord('a')
        
        counts1 = [0] * 26
        counts2 = [0] * 26
        for i in range(len(s1)):
            char = s1[i]
            counts1[index(char)] += 1
            char = s2[i]
            counts2[index(char)] += 1
        
        for i in range(len(s1), len(s2)):
            if counts1 == counts2:
                return True
            char = s2[i]
            counts2[index(char)] += 1
            char = s2[i - len(s1)]
            counts2[index(char)] -= 1
            
        return counts1 == counts2