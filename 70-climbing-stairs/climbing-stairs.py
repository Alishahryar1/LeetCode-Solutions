class Solution(object):
    def helper(self, n, ways):
        if n in ways:
            return ways[n]
        
        ways[n] = 0
        if n - 1 in ways:
            ways[n] += ways[n - 1]
        else:
            ways[n] += self.helper(n - 1, ways)
        
        if n - 2 in ways:
            ways[n] += ways[n - 2]
        else:
            ways[n] += self.helper(n - 2, ways)
        
        return ways[n]
    
    def climbStairs(self, n):
        if n <= 3:
            return n
        ways = {}
        ways[1] = 1
        ways[2] = 2
        ways[3] = 3
        return self.helper(n, ways)