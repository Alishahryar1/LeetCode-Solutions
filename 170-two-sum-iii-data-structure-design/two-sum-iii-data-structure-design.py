class TwoSum(object):

    def __init__(self):
        self.nums = []
        self.length = 0

    def add(self, number):
        """
        :type number: int
        :rtype: None
        """
        self.nums.append(number)
        self.length += 1
        i = self.length - 1
        while (i - 1 >= 0 and self.nums[i - 1] > self.nums[i]):
            self.nums[i - 1], self.nums[i] = self.nums[i], self.nums[i - 1]
            i -= 1

    def find(self, value):
        """
        :type value: int
        :rtype: bool
        """
        L = 0
        R = self.length - 1
        while L < R:
            total = self.nums[L] + self.nums[R]
            if total < value:
                L += 1
            elif total > value:
                R -= 1
            else:
                return True
        return False
        
# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)