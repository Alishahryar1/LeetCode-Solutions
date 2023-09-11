class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        s = list(s)
        goal = list(goal)
        if len(s) != len(goal):
            return False
        if s == goal:
            return True
        for i in range(len(s)):
            s.insert(0, s.pop())
            if s == goal:
                return True