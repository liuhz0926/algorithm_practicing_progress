class Result:
    def __init__(self):
        self.min_cost = float('inf')


class Solution:
    """
        2. DFS + 最优性剪枝
    @param n: an integer,denote the number of cities
    @param roads: a list of three-tuples,denote the road between cities
    @return: return the minimum cost to travel all cities
    """

    def minCost(self, n, roads):
        graph = self.construct_graph(n, roads)
        result = Result()
        self.dfs(n, graph, 1, [1], 0, set([1]), result)
        return result.min_cost

    def dfs(self, n, graph, city, path, cost, visited, result):
        if len(visited) == n:
            result.min_cost = min(result.min_cost, cost)
            return

        for next_city in graph[city]:
            if next_city in visited:
                continue
            if self.has_better_path(graph, path, next_city):
                continue

            # 证明是对的path，往下继续走
            visited.add(next_city)
            path.append(next_city)
            self.dfs(n, graph, next_city, path, cost + graph[city][next_city], visited, result)
            visited.remove(next_city)
            path.pop()

        return

    def construct_graph(self, n, roads):
        graph = {
            i: {j: float('inf') for j in range(1, n + 1)}
            for i in range(1, n + 1)
        }

        for A, B, c in roads:
            graph[A][B] = min(graph[A][B], c)
            graph[B][A] = min(graph[B][A], c)

        return graph

    def has_better_path(self, graph, path, next_city):
        for i in range(1, len(path)):
            origin_cost = graph[path[i - 1]][path[i]] + graph[path[-1]][next_city]
            swap_cost = graph[path[i - 1]][path[-1]] + graph[path[i]][next_city]
            # 证明随便一换就变小了，说明这个next city不对，不应该选这个
            if origin_cost > swap_cost:
                return True

        # 是对的path，应该加上这个next city
        return False
