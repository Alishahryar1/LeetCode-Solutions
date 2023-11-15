class Solution(object):
    def binarySearch(self, nums, L, R, target):
        while(L <= R):
            m = (L + R)//2
            if target < nums[m]:
                R = m - 1
            elif target > nums[m]:
                L = m + 1
            else:
                return m
        
        return -1
    
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        L, R = 0, n - 1
        minEle = float('inf')
        i = -1
        while (L <= R):
            if nums[L] < nums[R]:
                if nums[L] < minEle:
                    i, minEle = L, nums[L]
                break
            m = (L + R)//2
            if nums[m] < minEle:
                i, minEle = m, nums[m]
            if nums[L] <= nums[m]:
                L = m + 1
            else:
                R = m - 1
        

        a = self.binarySearch(nums, 0, i - 1, target)
        if a != -1:
            return a
        b = self.binarySearch(nums, i, n - 1, target)
        if b != -1:
            return b
        return -1