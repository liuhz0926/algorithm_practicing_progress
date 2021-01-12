import collections


class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """

    def sequenceReconstruction(self, org, seqs):
        # 保持队列中有且仅有一个元素
        graph = self.build_graph(seqs)
        order = self.topo_sorting(graph)

        return org == order

    def build_graph(self, seqs):
        graph = {}
        for seq in seqs:
            for node in seq:
                if node not in graph:
                    graph[node] = set()

        for seq in seqs:
            for i in range(1, len(seq)):
                graph[seq[i - 1]].add(seq[i])

        return graph

    def get_indegree(self, graph):
        indegree = {node: 0 for node in graph}

        for node in graph:
            for neighbor in graph[node]:
                indegree[neighbor] += 1

        return indegree

    def topo_sorting(self, graph):
        indegree = self.get_indegree(graph)

        queue = [node for node in indegree if indegree[node] == 0]

        order = []

        while queue:
            if len(queue) > 1:
                return None
            # 因为必须保证是一个所以直接用list pop，虽然其实是最后一个，但是就是当前的这个数字
            curt_node = queue.pop()
            order.append(curt_node)
            for neighbor in graph[curt_node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # 保证每个点都要有了
        if len(order) == len(graph):
            return order

        return None
