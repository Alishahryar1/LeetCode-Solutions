class Solution(object):
    def maxValue(self, n, index, maxSum):
        """
        :type n: int
        :type index: int
        :type maxSum: int
        :rtype: int
        """
        if n == 1:
            return maxSum
            
        temp1 = ((index)*(index + 1))//2
        temp2 = ((n - index - 1)*(n - index))//2
        
        left = 1
        right = maxSum - (n - 1)
        x = (left + right)//2
        while x >= 1:
            if x >= 1 + index:
                left_sum = index * x
                left_sum -= temp1
            else:
                left_sum = (index - x + 1)
                temp = (x*(x - 1))//2
                left_sum += temp
            
            if x >= (n - index):
                right_sum = (n - index - 1) * x
                right_sum -= temp2
            else:
                right_sum = n - index - x
                temp = (x*(x - 1))//2
                right_sum += temp
            total_sum = left_sum + right_sum + x
            if total_sum > maxSum:
                right = x
            elif total_sum < maxSum:
                left = x
            prev = x
            x = (left + right)//2
            if prev == x:
                return x