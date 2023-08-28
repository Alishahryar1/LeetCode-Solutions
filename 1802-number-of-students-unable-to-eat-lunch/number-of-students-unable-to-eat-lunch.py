class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        hungry = len(students)
        count = 0
        while count < hungry:
            if sandwiches[0] == students[0]:
                del sandwiches[0]
                del students[0]
                hungry -= 1
                count = 0
            else:
                students.append(students.pop(0))
                count += 1
        return hungry