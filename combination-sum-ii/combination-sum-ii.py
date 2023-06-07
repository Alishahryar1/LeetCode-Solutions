class Solution(object):
    def helper(self, candidates, target, visited, start):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        combinations = []
        for i in range(start, len(candidates)):
            if visited[i]:
                continue
            visited[i] = True
            num = candidates[i]
            if i > 0:
                if candidates[i - 1] == num and visited[i - 1] == False:
                    visited[i] = False
                    continue
            n = [num]
            if target == num:
                combinations.append(n)
            elif target - num > 0:
                new_c = self.helper(candidates, target - num, visited, i)
                [combinations.append(n + c) for c in new_c] 
            else:
                visited[i] = False
                break
            visited[i] = False
        
        return combinations
    
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        visited = [False] * len(candidates)
        for i, num in enumerate(candidates):
            if num > target:
                visited[i] = True
        combinations = self.helper(candidates, target, visited, 0)
        
        return combinations