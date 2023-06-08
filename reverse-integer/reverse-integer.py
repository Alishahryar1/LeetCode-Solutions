class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = x < 0
        x = abs(x)
        digits = []
        while x > 0:
            digits.append(x % 10) 
            x = x // 10
        
        L = len(digits)
        for i in reversed(range(L)):
            if negative:
                x -= digits[L - i - 1] * (10 ** i)
            else:
                x += digits[L - i - 1] * (10 ** i)
            if x > (2**31 - 1) or x < -2**31:
                    return 0
        return x