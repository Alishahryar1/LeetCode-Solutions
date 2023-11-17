class Solution(object):
    def validIndex(self, i, n):
        return i >= 0 and i < n

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m = len(nums1)
        n = len(nums2)
        total = m + n
        half = (m + n)//2
        L, R = 0, m - 1
        while True:
            mid = (L + R)//2
            i = half - mid - 2
            if self.validIndex(i, n) and self.validIndex(mid + 1, m) and nums2[i] > nums1[mid + 1]:
                L = mid + 1
            elif self.validIndex(i + 1, n) and self.validIndex(mid, m) and nums1[mid] > nums2[i + 1]:
                R = mid - 1
            else:
                if total % 2 == 1:
                    a = float('inf')
                    if mid + 1 < m:
                        a = min(a, nums1[mid + 1])
                    if i + 1 < n:
                        a = min(a, nums2[i + 1])
                    return a
                else:
                    a = float('-inf')
                    if mid >= 0 and mid < m:
                        a = max(a, nums1[mid])
                    if i >= 0 and i < n:
                        a = max(a, nums2[i])
                    b = float('inf')
                    if mid + 1 < m:
                        b = min(b, nums1[mid + 1])
                    if i + 1 < n:
                        b = min(b, nums2[i + 1])
                    return (a + b)/2.0



        
        return 0