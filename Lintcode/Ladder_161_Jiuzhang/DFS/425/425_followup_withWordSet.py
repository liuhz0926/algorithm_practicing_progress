KEYBOARD = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}


class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """

    def letterCombinations(self, digits, wordSet):
        if not digits:
            return []

        results = []

        # "abc" => a ab abc
        # 把所有的word在wordset里面，全部的prefix全都加进去，然后搜索的时候，看这个prefix在不在里面，在的话再继续查tw
        prefixSet = set([""])
        for word in wordSet:
            for i in range(1, len(word) + 1):
                prefixSet.add(word[:i])

        self.dfs(digits, 0, '', prefixSet, results)

        return results

    def dfs(self, digits, index, string, prefixSet, results):
        if string not in prefixSet:
            return

        if index == len(digits):
            results.append(string)
            return

        for letter in KEYBOARD[digits[index]]:
            self.dfs(digits, index + 1, string + letter, prefixSet, results)