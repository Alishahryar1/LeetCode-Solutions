from collections import deque

class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if node == None:
            return None
        head = Node(node.val)
        queue = deque()
        visited = {}
        queue.append((head.val, node, head))
        visited[head.val] = head
        while queue:
            for _ in range(len(queue)):
                _, curr, clone_curr = queue.popleft()
                for neighbor in curr.neighbors:
                    if neighbor.val in visited:
                        clone_curr.neighbors.append(visited[neighbor.val])
                        continue
                    clone_neighbor = Node(neighbor.val)
                    clone_curr.neighbors.append(clone_neighbor)
                    
                    queue.append((neighbor.val, neighbor, clone_neighbor))
                    visited[neighbor.val] = clone_neighbor
        
        return head