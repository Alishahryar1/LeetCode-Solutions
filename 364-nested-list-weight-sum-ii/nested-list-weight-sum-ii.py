# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
    def helper(self, nestedList, depth):
        if nestedList.isInteger():
            Integer = nestedList.getInteger()
            return Integer, depth, depth * Integer
        
        List = nestedList.getList()
        
        integerSum, maxDepth, weightedSum = 0, depth, 0
        for item in List:
            res = self.helper(item, depth + 1)
            integerSum += res[0]
            maxDepth = max(res[1], maxDepth)
            weightedSum += res[2]

        return integerSum, maxDepth, weightedSum
    
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        integerSum, maxDepth, weightedSum = 0,0,0
        for item in nestedList:
            res = self.helper(item, 1)
            integerSum += res[0]
            maxDepth = max(res[1], maxDepth)
            weightedSum += res[2]
        
        return (maxDepth + 1) * integerSum - weightedSum