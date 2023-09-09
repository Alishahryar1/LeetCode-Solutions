class Solution(object):
    def courseFinishable(self, pre_req, adj_list, visited):
        if len(adj_list[pre_req]) == 0:
            return True
        if pre_req in visited:
            return False
        visited.add(pre_req)
        for course in adj_list[pre_req]:
            if not self.courseFinishable(course, adj_list, visited):
                return False
        
        visited.remove(pre_req)
        adj_list[pre_req] = []
        return True
        
    
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if len(prerequisites) == 0:
            return True
        adj_list = {}
        for a, b in prerequisites:
            if a not in adj_list:
                adj_list[a] = []
            if b not in adj_list:
                adj_list[b] = []
            adj_list[a].append(b)
        
        for course in adj_list.keys():
            if not self.courseFinishable(course, adj_list, set()):
                return False
        return True