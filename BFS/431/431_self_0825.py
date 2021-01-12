"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""

from collections import deque


class Solution:
    """
    @param {UndirectedGraphNode[]} nodes a array of undirected graph node
    @return {int[][]} a connected set of a undirected graph
    """

    def connectedSet(self, nodes):
        result = []
        visited = set()

        for node in nodes:
            if node not in visited:
                subgraph = []
                self.bfs(node, visited, subgraph)
                result.append(sorted(subgraph))

        return result

    def bfs(self, node, visited, subgraph):
        queue = deque([node])
        visited.add(node)

        while queue:
            curt_node = queue.popleft()

            # 必须add label 因为 curt node是object。 最后要的答案是123。 object没办法sorted 所以出问题
            subgraph.append(curt_node.label)
            for neighbor in curt_node.neighbors:
                if neighbor in visited:
                    continue
                queue.append(neighbor)
                visited.add(neighbor)
