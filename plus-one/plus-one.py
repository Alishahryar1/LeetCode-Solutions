class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        for i in reversed(range(len(digits))):
            num += digits[len(digits) - i - 1] * (10 ** i)
        num += 1
        digits_new = []
        for digit in str(num):
            digits_new.append(int(digit))
        
        return  digits_new