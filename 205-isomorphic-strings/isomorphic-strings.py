class Solution(object):
    def transform(self, string):
        letterMap = {}
        res = []
        for i, s in enumerate(string):
            if s not in letterMap:
                letterMap[s] = i
            res.append(letterMap[s])
        return res

    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        List1, List2 = self.transform(s), self.transform(t)
        return List1 == List2