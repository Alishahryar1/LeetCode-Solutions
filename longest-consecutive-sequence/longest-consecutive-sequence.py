class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        partofnums = {}
        for num in nums:
            partofnums[num] = 0
            partofnums[num + 1] = -1
        
        for num in nums:
            partofnums[num] = 0

        length_max = 0
        for num in nums:
            if partofnums[num] > 0:
                continue
            length = 0
            curr_num = num
            assigned = False
            while partofnums[curr_num] >= 0:
                if partofnums[curr_num] > 0: 
                    length += partofnums[curr_num]
                    partofnums[num] = length
                    assigned = True
                    break
                length += 1
                curr_num += 1
            if not assigned:
                for curr_num in range(num, num + length):
                    partofnums[curr_num] = length
                
            length_max = max(length, length_max)
        return length_max