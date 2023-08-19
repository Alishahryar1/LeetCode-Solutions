class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        List1 = []
        List2 = []
        for i in range(265):
            List1.append([])
            List2.append([])
        for i in range(len(s)):
            List1[ord(s[i])].append(i)
        for i in range(len(t)):
            List2[ord(t[i])].append(i)
        for i in range(len(List1)):
            if List1[i] == []:
                continue
            for j in range(len(List2)):
                if List1[i] == List2[j]:
                    List2[j] = []
                    break
            else:
                return False
        return True