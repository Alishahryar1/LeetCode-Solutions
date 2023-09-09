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
        queue.append((node, head))
        visited[head.val] = head
        while queue:
            for _ in range(len(queue)):
                curr, clone_curr = queue.popleft()
                for neighbor in curr.neighbors:
                    if neighbor.val in visited:
                        clone_curr.neighbors.append(visited[neighbor.val])
                        continue
                    clone_neighbor = Node(neighbor.val)
                    clone_curr.neighbors.append(clone_neighbor)
                    queue.append((neighbor, clone_neighbor))
                    visited[neighbor.val] = clone_neighbor
        
        return head