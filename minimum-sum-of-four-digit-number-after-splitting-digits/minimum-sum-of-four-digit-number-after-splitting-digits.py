class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        m = num + 1
        num = list(str(num))
        L = len(num)
        p_s = []
        for i in range(L):
            for j in range(L):
                for k in range(L):
                    for l in range(L):
                        if i == j or i == k or i == l or j == k or j == l or k == l: 
                            continue
                        p_s.append(num[i] + num[j] + num[k] + num[l])
        
        for p in p_s:
            for i in range(1, L):
                n = int(p[:i]) + int(''.join(p[i:]))
                m = min(m, n)
        return m