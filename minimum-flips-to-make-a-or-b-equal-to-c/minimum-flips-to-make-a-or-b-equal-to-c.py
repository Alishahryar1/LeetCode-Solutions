class Solution(object):
    def minFlips(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        bit_a = []
        while a > 0:
            bit_a.insert(0, a % 2)
            a = a // 2
        
        bit_b = []
        while b > 0:
            bit_b.insert(0, b % 2)
            b = b // 2

        bit_c = []
        while c > 0:
            bit_c.insert(0, c % 2)
            c = c // 2
        
        max_len = max(len(bit_a), len(bit_b), len(bit_c))
        if len(bit_a) < max_len:
            bit_a = [0] * (max_len - len(bit_a)) + bit_a
        if len(bit_b) < max_len:
            bit_b = [0] * (max_len - len(bit_b)) + bit_b
        if len(bit_c) < max_len:
            bit_c = [0] * (max_len - len(bit_c)) + bit_c
        
        flips = 0
        for i in range(len(bit_a)):
            if bit_c[i] == 1:
                if bit_a[i] == 0 and bit_b[i] == 0:
                    flips += 1
            elif bit_c[i] == 0:
                if bit_a[i] == 1 and bit_b[i] == 1:
                    flips += 2
                elif bit_a[i] + bit_b[i] == 1:
                    flips += 1
        return flips

