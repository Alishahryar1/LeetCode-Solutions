class Solution(object):
    def helper(self, candidates, target, output, subset):
        if target < 0:
            return
        if target == 0:
            output.append(subset)
            return
        for i, num in enumerate(candidates):
            self.helper(candidates[i:], target - num, output, subset + [num])
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        output = []
        self.helper(candidates, target, output, [])
        return output