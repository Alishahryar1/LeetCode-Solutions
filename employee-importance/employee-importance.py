"""
# Definition for Employee.
class Employee(object):
    def __init__(self, id, importance, subordinates):
    	#################
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        #################
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution(object):
    def helper(self, employees_map, id):

        total_importance = employees_map[id]['imp']
        
        if len(employees_map[id]['subs']) == 0:
            return total_importance
        
        for sub in employees_map[id]['subs']:
            total_importance += self.helper(employees_map, sub)
        
        return total_importance 
    
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        employees_map = {}
        for employee in employees:
            employees_map[employee.id] = {'imp':employee.importance, 'subs':employee.subordinates}

        return self.helper(employees_map, id)