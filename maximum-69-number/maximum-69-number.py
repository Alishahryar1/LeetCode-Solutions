class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        num_list = list(str(num))
        for i, digit in enumerate(num_list):
            if digit == '6':
                num_list[i] = '9'
                break
        return int(''.join(num_list))