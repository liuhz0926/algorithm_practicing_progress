class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """

    def ladderLength(self, start, end, dict):
        # 优化版本
        dict.add(end)
        queue = collections.deque([start])
        # 这里不用visted 因为distance的key就是visted。
        distance = {start: 1}
        # value表示 层数

        while queue:
            curt_word = queue.popleft()
            if curt_word == end:
                return distance[curt_word]
            for next_word in self.get_next_words(curt_word):
                # 换另一种写法。or continue这样锁紧少一点
                if next_word not in distance and next_word in dict:
                    queue.append(next_word)
                    distance[next_word] = distance[curt_word] + 1

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
