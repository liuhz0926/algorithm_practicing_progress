class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """

    def findLadders(self, start, end, dict):
        # 确保dictionary里面有start和end
        dict.add(start)
        dict.add(end)
        distance = {}

        # BFS：求出所有点到终点的距离（其实就是终点到所有点的距离
        self.bfs(end, distance, dict)

        # DFS：沿着离终点越来越近的路线找到所有路径
        # dfs 只选择 distance nextword 和 curtword差1的路
        results = []
        path = [start]
        self.dfs(start, end, distance, dict, path, results)

        return results

    def bfs(self, root, distance, dict):
        # 一个正常bfs 求所有点到root的距离
        # 和120题写的几乎一样，
        # 唯一不一样的地方是root 的distance 120记做1，是因为那里我们要找的是最后root的length，所以root算一个点
        # 而这里只要记录每个点到root有多远就可以了，所以可以从0开始算
        distance[root] = 0
        queue = collections.deque([root])
        while queue:
            curt_word = queue.popleft()
            for next_word in self.get_all_next_words(curt_word, dict):
                if next_word in distance:
                    continue
                distance[next_word] = distance[curt_word] + 1
                queue.append(next_word)

    def get_all_next_words(self, word, dict):
        # 和120几乎一样，就是我们在审查next word的时候就审查dict里面有没有这个词。
        # 这样写要比120快一点，因为next words不会特别多，在bfs循环next word的时候循环的要少一些
        next_words = []
        for i in range(len(word)):
            left, right = word[:i], word[i + 1:]
            for char in 'abcdefghijklmnopqrstuvwxyz':
                next_word = left + char + right
                if next_word != word and next_word in dict:
                    next_words.append(next_word)

        return next_words

    def dfs(self, curt_word, target_word, distance, dict, path, results):
        if curt_word == target_word:
            results.append(list(path))

        for next_word in self.get_all_next_words(curt_word, dict):
            # 我们只选择-1的路走
            if distance[next_word] != distance[curt_word] - 1:
                continue
            path.append(next_word)
            self.dfs(next_word, target_word, distance, dict, path, results)
            # backtracking
            path.pop()

