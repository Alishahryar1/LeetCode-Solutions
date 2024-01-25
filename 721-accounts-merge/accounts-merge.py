class UnionFind():
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, n):
        p = self.par[n]
        while (p != self.par[p]):
            #path compression
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p2] > self.rank[p1]:
            self.par[p1] = p2
        else:
            self.par[p2] = p1
            self.rank[p1] += 1
        return True

class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        UF = UnionFind(len(accounts))
        hashmap = {}
        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in hashmap:
                    UF.union(i, hashmap[e])
                else:
                    hashmap[e] = i
        ans_map = {}
        for e, i in hashmap.items():
            group = UF.find(i)
            if group not in ans_map:
                ans_map[group] = []
            ans_map[group].append(e)
        ans = []
        for i, L in ans_map.items():
            ans.append([accounts[i][0]] + sorted(list(L)))


        return ans
        