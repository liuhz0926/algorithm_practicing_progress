class Solution:
    """
    @param: chars: The letter array you should sort by Case
    @return: nothing
    """

    def sortLetters(self, chars):
        # 此题input并不是一个string。而是一个array。虽然输入形式是一个字符串。
        # python里面的字符串是不能swap的。因为string是immutable的
        left, right = 0, len(chars) - 1
        while left <= right:
            while left <= right and chars[left].islower():
                left += 1
            while left <= right and chars[right].isupper():
                right -= 1
            if left <= right:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1

        return chars
