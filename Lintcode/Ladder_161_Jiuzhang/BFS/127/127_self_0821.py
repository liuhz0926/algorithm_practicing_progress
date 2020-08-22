"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """

    def topSort(self, graph):
        indegree = self.get_indegree(graph)

        queue = collections.deque([node for node in indegree if indegree[node] == 0])
        order = []

        while queue:
            curt_node = queue.popleft()
            order.append(curt_node)
            for neighbor in curt_node.neighbors:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return order

    def get_indegree(self, graph):
        indegree = {node: 0 for node in graph}
        for node in graph:
            for neighbor in node.neighbors:
                indegree[neighbor] += 1

        return indegree