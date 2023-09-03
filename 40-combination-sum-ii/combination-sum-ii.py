class Solution(object):

    def helper(self, candidates, target, output, subset):
        if target < 0:
            return
        if target == 0:
            output.append(subset)
            return
        
        for i, num in enumerate(candidates):
            if i > 0 and num == candidates[i - 1]:
                continue
            self.helper(candidates[i + 1:], target - num, output, subset + [num])

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        output = []
        candidates.sort()
        self.helper(candidates, target, output, [])
        return output       