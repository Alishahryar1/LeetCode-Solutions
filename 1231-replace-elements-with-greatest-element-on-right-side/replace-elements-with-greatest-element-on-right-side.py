class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        max_num = arr[-1]
        new_arr = [0] * len(arr)
        new_arr[-1] = -1
        for i in reversed(range(len(arr) - 1)):
            max_num = max(max_num, arr[i + 1])
            new_arr[i] = max_num
        return new_arr