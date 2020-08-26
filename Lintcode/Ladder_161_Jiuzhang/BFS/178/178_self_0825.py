import collections
class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """


    def validTree(self, n, edges):

        # 这一行判断是不是有环，因为如果有多余的边。就会出现环，因为保证每个点都只有一条边。所以是n-1条边
        if len(edges) != n - 1:
            return False

        graph = self.make_graph(n, edges)

        queue = collections.deque([0])
        visited = set([0])

        while queue:
            curt_node = queue.popleft()
            for neighbor in graph[curt_node]:
                if neighbor in visited:
                    continue
                queue.append(neighbor)
                visited.add(neighbor)

        return len(visited) == n

    def make_graph(self, n, edges):
        graph = {node: set() for node in range(n)}

        for node1, node2 in edges:
            graph[node1].add(node2)
            graph[node2].add(node1)

        return graph
