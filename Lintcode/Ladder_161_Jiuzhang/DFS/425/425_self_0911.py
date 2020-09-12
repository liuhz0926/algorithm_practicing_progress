KEYBOARD = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}


class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """

    def letterCombinations(self, digits):
        if not digits:
            return []

        results = []
        self.dfs(digits, 0, [], results)
        return results

    def dfs(self, digits, index, combination, results):
        if len(combination) == len(digits):
            results.append(''.join(combination))
            return

        letters = KEYBOARD[digits[index]]

        for char in letters:
            combination.append(char)
            self.dfs(digits, index + 1, combination, results)
            combination.pop()

        return

