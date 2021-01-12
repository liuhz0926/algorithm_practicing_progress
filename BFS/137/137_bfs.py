"""
class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""
import collections


class Solution:
    """
    @param node: A undirected graph node
    @return: A undirected graph node
    """

    def cloneGraph(self, node):
        root = node
        if not root:
            return None

        # Step 1: use bfs to get all nodes
        nodes = self.bfs_get_nodes(root)

        # copy node into a mapping hash map dictionary where key is the old nodes
        # and value is the new node we create/copy by using the old nodes labels and UndirectedGraphNode class
        mapping = {}
        for old_node in nodes:
            mapping[old_node] = UndirectedGraphNode(old_node.label)

        # copy edges by copy neighbors into the mapping
        # 我们要要把旧的neighbors全部加到new node（value）上面
        for old_node in nodes:
            new_node = mapping[old_node]
            for old_neighbor in old_node.neighbors:
                # because all nodes are in the mapping we need to find the correspoding value for the old neighbor
                new_neighbor = mapping[old_neighbor]
                # setup the new neighbor
                new_node.neighbors.append(new_neighbor)

        return mapping[root]

    def bfs_get_nodes(self, node):
        queue = collections.deque([node])
        result = set([node])
        while queue:
            current_node = queue.popleft()
            for neighbor in current_node.neighbors:
                if neighbor not in result:
                    result.add(neighbor)
                    queue.append(neighbor)
        return result