class Solution(object):
    def canThreePartsEqualSum(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        left_sum = 0
        right_sum = sum(arr)
        for i in range(len(arr)):
            current_num = arr[i]
            left_sum += current_num
            right_sum -= current_num
            if right_sum == 2 * left_sum:
                left_sum = 0
                for j in range(i + 1, len(arr)):
                    left_sum += arr[j]
                    right_sum -= arr[j]
                    if right_sum == left_sum and j < len(arr) - 1:
                        return True
                break
        return False