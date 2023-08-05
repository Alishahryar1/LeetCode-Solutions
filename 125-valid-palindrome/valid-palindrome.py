class Solution(object):
    def isAlphabet(self, x):
        order = ord(x)
        return (order >= 97 and order <= 122) or (order >= 65 and order <= 90) 
    
    def isDigit(self, x):
        order = ord(x)
        return order >= 48 and order <= 57
    
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s_new = [x.lower() for x in s if self.isAlphabet(x) or self.isDigit(x)]
        left = 0
        right = len(s_new) - 1
        while left < right:
            if s_new[left] != s_new[right]:
                return False
            left += 1
            right -= 1
        
        return True