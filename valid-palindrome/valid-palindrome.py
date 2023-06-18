class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        s_new = [x for x in s if (ord(x) >= 97 and ord(x) <= 122) or (ord(x) >= 48 and ord(x) <= 57)]
        left = 0
        right = len(s_new) - 1
        while left < right:
            if s_new[left] != s_new[right]:
                return False
            left += 1
            right -= 1
        return True