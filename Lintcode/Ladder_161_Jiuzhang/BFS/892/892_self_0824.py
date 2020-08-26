from heapq import heappush, heappop, heapify


class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """

    def alienOrder(self, words):
        graph = self.make_graph(words)
        return self.topo_sorting(graph)

    def make_graph(self, words):
        graph = {}

        # node
        for word in words:
            for char in word:
                if char not in graph:
                    graph[char] = set()

        # edge
        for i in range(len(words) - 1):
            for j in range(min(len(words[i]), len(words[i + 1]))):
                if words[i][j] != words[i + 1][j]:
                    graph[words[i][j]].add(words[i + 1][j])
                    # 注意只看这一个字母就不用查这两个单词了。查下一组
                    break
                if j == min(len(words[i]), len(words[i + 1])) - 1:
                    if len(words[i]) > len(words[i + 1]):
                        # abc不能在ab的前面。关于notice的第二条
                        # 如果到最后一位了。他俩都相同。但是前面的那个word要长。说明不对
                        return None

        return graph

    def get_indegrees(self, graph):
        indegrees = {node: 0 for node in graph}

        for node in graph:
            for neighbor in graph[node]:
                indegrees[neighbor] += 1

        return indegrees

    def topo_sorting(self, graph):

        if not graph:
            return ""

        indegrees = self.get_indegrees(graph)

        queue = [node for node in graph if indegrees[node] == 0]
        # 用heapq是保证他可以linear 的每次pop的都是最小的最头按顺序的字母
        heapify(queue)
        order = ""

        while queue:
            curt_node = heappop(queue)
            order += curt_node
            for neighbor in graph[curt_node]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    heappush(queue, neighbor)

        # 一定要判断order 的长度是不是所有的node！
        if len(order) == len(graph):
            return order

        return ""
