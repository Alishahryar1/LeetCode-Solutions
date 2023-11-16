class TimeMap(object):

    def __init__(self):
        self.hashMap = {}

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key not in self.hashMap:
            self.hashMap[key] = []
        self.hashMap[key].append((value, timestamp))
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key not in self.hashMap:
            return ""
        n = len(self.hashMap[key])
        L, R = 0, n - 1
        maxtimestamp = 0
        i = -1
        while(L <= R):
            m = (L + R)//2
            _, currtimestamp = self.hashMap[key][m]
            if currtimestamp <= timestamp and currtimestamp > maxtimestamp:
                maxtimestamp = currtimestamp
                i = m
            if currtimestamp < timestamp:
                L = m + 1
            elif timestamp < currtimestamp:
                R = m - 1
            else:
                maxtimestamp = currtimestamp
                i = m
                break
        return self.hashMap[key][i][0] if i >= 0 else ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)