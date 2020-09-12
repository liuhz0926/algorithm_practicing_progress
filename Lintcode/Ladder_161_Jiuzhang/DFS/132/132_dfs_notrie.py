DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


class Solution:
    """
    for 矩阵里面每个单词每个方向，check是否在词典里，下一层循环前check是不是在prefix里面
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """

    def wordSearchII(self, board, words):
        if not board or len(words) == 0:
            return []

        # Make Prefix list for each word in words
        # 去重 （也可以写成range(1, len(word) + 1), add word[:i]
        word_set = set(words)
        prefix_set = set()
        for word in word_set:
            for i in range(len(word)):
                # 因为不到i+1位置
                prefix_set.add(word[:i + 1])

        # 这里set来去重
        results = set()
        # 原来矩阵题
        # 找到一个后，visited要从头开始
        # 和原来bfs矩阵题很像，因为要考虑每一个点作为初始点。所以要for循环每一个初始点
        for i in range(len(board)):
            for j in range(len(board[0])):
                # 每一个单词要重启visited
                start_char = board[i][j]
                visited = set([(i, j)])
                self.dfs(i, j, board, word_set, prefix_set, start_char, visited, results)

        return list(results)

    def dfs(self, x, y, board, word_set, prefix_set, word, visited, results):
        # 出口是这个。不是说这个单词在里面，因为也有可能出现he是一个词 hellow也是一个词，所以在wordset里面不能直接return
        if word not in prefix_set:
            return

        if word in word_set:
            results.add(str(word))

        for dx, dy in DIRECTIONS:
            next_x = dx + x
            next_y = dy + y

            # 判断出没出界
            if not self.is_inside(next_x, next_y, board):
                continue

            # 判断在没在visited里面：
            if (next_x, next_y) in visited:
                continue

            # 按照常规dfs
            visited.add((next_x, next_y))
            self.dfs(next_x, next_y, board, word_set, prefix_set, word + board[next_x][next_y], visited, results)

            # backtracking
            visited.remove((next_x, next_y))
            # 注意这里是for loop四个方向， 所以不用倒退往回走。这个点访问完会自动选择下一个方向，
            # 四个方向都走完，会回到上一个点，然后哪里还有四个方向

        return

    def is_inside(self, x, y, board):
        return 0 <= x < len(board) and 0 <= y < len(board[0])