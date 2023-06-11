class SnapshotArray(object):

    def __init__(self, length):
        """
        :type length: int
        """
        self.sets = [{}]
        self.snap_id = 0
        self.length = length

    def set(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        self.sets[self.snap_id][index] = val

    def snap(self):
        """
        :rtype: int
        """
        self.sets.append({})
        self.snap_id += 1

        return self.snap_id - 1
      
    def get(self, index, snap_id):
        """
        :type index: int
        :type snap_id: int
        :rtype: int
        """
        while index not in self.sets[snap_id] and snap_id >= 0:
            snap_id -= 1
        
        if snap_id < 0:
            return 0
        else:
            return self.sets[snap_id][index]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)