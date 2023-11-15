class Solution(object):
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
        
        L, R = i, n + i - 1
        while (L <= R):
            m = (L + R)//2
            index = m % n
            if target < nums[index]:
                R = m - 1
            elif target > nums[index]:
                L = m + 1
            else:
                return index
        
        return -1