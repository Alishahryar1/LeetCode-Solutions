class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        hashmap = {}

        for i in range(len(nums)):
            target = -nums[i]
            left = 0
            right = len(nums) - 1
            while left < right:
                if left == i:
                    left += 1
                    continue
                elif right == i:
                    right -= 1
                    continue
                two_sum = nums[left] + nums[right]
                if two_sum == target:
                    if nums[i] < nums[left]:
                        a = [nums[i], nums[left], nums[right]]
                    elif nums[i] < nums[right]:
                        a = [nums[left], nums[i],nums[right]]
                    else:
                        a = [nums[left], nums[right], nums[i]]
                    hashmap[tuple(a)] = a
                    left += 1
                    right -= 1
                elif two_sum < target:
                    left += 1
                else:
                    right -= 1

        return list(hashmap.values())