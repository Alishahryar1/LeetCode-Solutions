class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        if len(t) > len(s):
            return ""
        
        Tcounts, Scounts = {}, {}
        for l in t:
            if l not in Tcounts:
                Tcounts[l] = 0
            if l not in Scounts:
                Scounts[l] = 0
            Tcounts[l] += 1
        
        L, R, need, have = 0, 0, len(Tcounts), 0
        res = {'L': 0, 'R': len(s)}
        while (R < len(s)):
            if s[R] in Scounts:
                Scounts[s[R]] += 1
                if Scounts[s[R]] == Tcounts[s[R]]:
                    have += 1  
            while (have == need):
                if R - L + 1 < res['R'] - res['L'] + 1:
                    res['L'], res['R'] = L, R
                if s[L] in Scounts:
                    Scounts[s[L]] -= 1
                    if Scounts[s[L]] < Tcounts[s[L]]:
                        have -= 1
                L += 1
            R += 1
        
        return "" if (res['R'] == len(s)) else "".join(s[res['L']:res['R'] + 1])