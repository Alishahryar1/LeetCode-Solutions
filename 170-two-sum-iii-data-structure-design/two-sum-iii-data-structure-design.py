class TwoSum(object):

    def __init__(self):
        self.num_counts = {}

    def add(self, number):
        """
        :type number: int
        :rtype: None
        """
        if number not in self.num_counts:
            self.num_counts[number] = 0
        self.num_counts[number] += 1

    def find(self, value):
        """
        :type value: int
        :rtype: bool
        """
        for num, count in self.num_counts.items():
            diff = value - num
            if diff in self.num_counts:
                if diff != num or (diff == num and self.num_counts[diff] > 1):
                    return True

        return False
        
# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)