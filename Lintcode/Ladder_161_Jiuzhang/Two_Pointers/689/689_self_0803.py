class Solution:
    """
    @param: : the root of tree
    @param: : the target sum
    @return: two numbers from tree which sum is n
    """

    def twoSum(self, root, n):
        # write your code here
        traverse_lst = []
        self.traverse(root, traverse_lst)

        left, right = 0, len(traverse_lst) - 1
        while left < right:
            if traverse_lst[left] + traverse_lst[right] < n:
                left += 1
            elif traverse_lst[left] + traverse_lst[right] > n:
                right -= 1
            else:
                return [traverse_lst[left], traverse_lst[right]]

    def traverse(self, root, traverse_lst):
        # BST in order recursive
        if not root:
            return
        self.traverse(root.left, traverse_lst)
        traverse_lst.append(root.val)
        self.traverse(root.right, traverse_lst)