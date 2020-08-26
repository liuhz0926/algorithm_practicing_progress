"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: graph: a list of Undirected graph node
    @param: values: a hash mapping, <UndirectedGraphNode, (int)value>
    @param: node: an Undirected graph node
    @param: target: An integer
    @return: a node
    """

    def searchNode(self, graph, values, node, target):
        # write your code here
        if not graph:
            return None

        if values[node] == target:
            return node

        queue = collections.deque([node])
        visited = set([node])

        while queue:
            curt_node = queue.popleft()
            if values[curt_node] == target:
                return curt_node

            for neighbor in curt_node.neighbors:
                if neighbor in visited:
                    continue
                queue.append(neighbor)
                visited.add(neighbor)

        return None
