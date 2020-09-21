class Solution:
    """
    @param strs: A list of strings
    @return: A list of strings
    """

    def anagrams(self, strs):

        # 先循环看每一个string的个体有没有出现过（九章的答案是以记录sort后的list转换为string做key）
        # 这里用的tuple
        set_to_input = {}
        for string in strs:
            # string sort 后直接是个list
            key = tuple(sorted(string))
            if key not in set_to_input:
                set_to_input[key] = [string]
            else:
                set_to_input[key].append(string)

        # 我们只要出现过两次以上的。一次的不算
        result = []
        for _, inputs in set_to_input.items():
            if len(inputs) > 1:
                result += inputs

        return result