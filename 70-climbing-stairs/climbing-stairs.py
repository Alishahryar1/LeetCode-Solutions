class Solution(object):
    def helper(self, n, ways):
        if ways[n - 1] > 0:
            return ways[n - 1]
        
        if ways[n - 2] > 0:
            ways[n - 1] += ways[n - 2]
        else:
            ways[n - 1] += self.helper(n - 1, ways)
        
        if ways[n - 3] > 0:
            ways[n - 1] += ways[n - 3]
        else:
            ways[n - 1] += self.helper(n - 2, ways)
        
        return ways[n - 1]
    
    def climbStairs(self, n):
        if n <= 3:
            return n
        ways = [0] * n
        ways[0] = 1
        ways[1] = 2
        ways[2] = 3
        return self.helper(n, ways)