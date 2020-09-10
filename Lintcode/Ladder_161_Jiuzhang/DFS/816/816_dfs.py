class Result:
    """
        必须需要这个class，否则 object这个参数无法进行修改
        因为如果不return，就不能pass through functions

    """

    def __init__(self):
        self.min_cost = float('inf')


class Solution:
    """
    1 暴力搜索法

    @param n: an integer,denote the number of cities
    @param roads: a list of three-tuples,denote the road between cities
    @return: return the minimum cost to travel all cities
    """

    def minCost(self, n, roads):
        graph = self.construct_graph(n, roads)
        result = Result()
        self.dfs(1, n, set([1]), 0, graph, result)
        return result.min_cost

    # 递归的定义：city 当前城市，n 一共有多少城市，visited去过了哪些城市，cost去过的总花费是多少，graph当前的图，min_cost记录最优cost
    def dfs(self, city, n, visited, cost, graph, result):
        # 递归的出口：visited里所有的店都访问过了，记录当前cost，看看是不是最小，return
        if len(visited) == n:
            result.min_cost = min(result.min_cost, cost)
            return

        # 递归的拆解：去找下一个city
        for next_city in graph[city]:
            if next_city in visited:
                continue
            visited.add(next_city)
            self.dfs(next_city, n, visited, cost + graph[city][next_city], graph, result)
            # backtracking
            visited.remove(next_city)

    def construct_graph(self, n, roads):
        graph = {node:
                     {neighbor: float('inf') for neighbor in range(1, n + 1)}
                 for node in range(1, n + 1)
                 }

        for A, B, c in roads:
            graph[A][B] = min(graph[A][B], c)
            graph[B][A] = min(graph[B][A], c)

        return graph