class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = s.replace('-','')
        output = ""
        count = 0
        for i in reversed(range(len(s))):
            if count % k == 0 and count > 0:
                output = '-' + output
                count = 0
            output = s[i].upper() + output
            count += 1
        return output