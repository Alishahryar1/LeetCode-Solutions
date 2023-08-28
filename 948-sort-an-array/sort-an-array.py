class Solution(object):
    def merge(self, L, m, R, nums):
        left_arr = nums[L:m]
        right_arr = nums[m:R]
        i = L
        i1 = 0
        i2 = 0
        while (i1 < len(left_arr) and i2 < len(right_arr)):
            if left_arr[i1] <= right_arr[i2]:
                nums[i] = left_arr[i1]
                i1 += 1
            else:
                nums[i] = right_arr[i2]
                i2 += 1
            i += 1
        if i1 == len(left_arr):
            nums[i:R] = right_arr[i2:]
        else:
            nums[i:R] = left_arr[i1:]

    def mergeSort(self, L, R, nums):
        if R - L == 1:
            return 
        m = (L + R)//2
        self.mergeSort(L, m, nums)
        self.mergeSort(m, R, nums)
        self.merge(L, m, R, nums)
    
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        self.mergeSort(0, len(nums), nums)
        return nums