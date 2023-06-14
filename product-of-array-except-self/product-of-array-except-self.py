class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        L = len(nums)
        left_products = [0] * L
        left_products[0] = 1
        left_products[1] = nums[0]
        for i in range(2, L):
            left_products[i] = nums[i - 1] * left_products[i - 1]
        
        right_products = [0] * L
        right_products[L - 1] = 1
        right_products[L - 2] = nums[L - 1]
        for i in reversed(range(L - 2)):
            right_products[i] = nums[i + 1] * right_products[i + 1]

        ans = []
        for i in range(L):
            ans.append(right_products[i] * left_products[i])
        return ans