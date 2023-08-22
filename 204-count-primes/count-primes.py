class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        isPrime = [False] * n
        i = 2
        count = 1
        while i < n:
            j = i + i
            while j < n:
                isPrime[j] = True
                j += i
            j = i + 1
            while j < n:
                if isPrime[j]:
                    j += 1
                else:
                    count += 1
                    break
            i = j
            
        return count