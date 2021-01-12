class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """

    def ladderLength(self, start, end, dict):
        dict.add(end)
        # use bfs to search one level by one level until the end word appears
        queue = collections.deque([start])
        # distance is the level
        visited = set([start])
        distance = 0

        while queue:
            distance += 1
            # in current level: loop in all words in current
            for _ in range(len(queue)):
                curt_word = queue.popleft()
                if curt_word == end:
                    return distance

                # search for next word
                for next_word in self.get_next_words(curt_word):
                    if next_word not in dict or next_word in visited:
                        continue
                    # 在词库里的且没有visited的
                    visited.add(next_word)
                    queue.append(next_word)
        # 没有
        return 0

    def get_next_words(self, word):
        next_words = []
        for i in range(len(word)):
            left, right = word[:i], word[i + 1:]
            for char in 'abcdefghijklmnopqrstuvwxyz':
                if word[i] == char:
                    continue
                next_words.append(left + char + right)
        return next_words
