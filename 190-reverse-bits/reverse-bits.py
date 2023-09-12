class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        i = 31
        num = 0
        while n > 0:
            num += (n & 1) * (2 ** i)
            n = n >> 1
            i -= 1
        
        return num