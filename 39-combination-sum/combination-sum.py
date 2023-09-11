class Solution(object):
    def helper(self, candidates, target, output, subset, i):
        if target < 0:
            return
        if target == 0:
            output.append(subset)
            return
        for j in range(i, len(candidates)):
            self.helper(candidates, target - candidates[j], output, subset + [candidates[j]], j)
    
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        output = []
        self.helper(candidates, target, output, [], 0)
        return output