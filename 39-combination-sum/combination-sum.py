class Solution(object):
    def helper(self, i, candidates, target, stack, res):
        if target < 0 or i == len(candidates):
            return
        if target == 0:
            res.append(stack[:])
            return 
        self.helper(i + 1, candidates, target, stack, res)
        stack.append(candidates[i])
        self.helper(i, candidates, target - candidates[i], stack, res)
        stack.pop()
    
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        self.helper(0, candidates, target, [], res)
        return res