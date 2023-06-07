class Solution(object):
    def helper(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        combinations = []
        for num in candidates:
            n = [num]
            if target == num:
                combinations.append(n)
            elif target - num > 0:
                new_c = self.combinationSum(candidates, target - num)
                for c in new_c:
                    a = n + c
                    a.sort()
                    combinations.append(a)
        
        return combinations

    def combinationSum(self, candidates, target):
        combinations = self.helper(candidates, target)
        ans = []
        for c in combinations:
            if c not in ans:
                ans.append(c)
        return ans