class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 0:
            return []
        output = [str(nums[0])]
        if len(nums) == 1:
            return output
        index = len(output[0])
        count = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                output[count] = output[count][:index] + '->' + str(nums[i])
            else:
                output.append(str(nums[i]))
                count += 1
                index = len(output[count])
        return output