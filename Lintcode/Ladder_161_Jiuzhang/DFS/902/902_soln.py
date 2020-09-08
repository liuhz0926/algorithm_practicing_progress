"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """

    def kthSmallest(self, root, k):
        # use binary tree iterator
        # 加这个是因为先把他pop出去算一次，然后把root加进来了。root是他的right
        # 然后再pop k - 1次，最后剩下的倒数第一个是k次。这个方法减少了先把所有root的left加进去
        dummy = TreeNode(0)
        dummy.right = root
        stack = [dummy]

        for i in range(k):
            node = stack.pop()
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
            if not stack:
                return None

        return stack[-1].val


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """

    def kthSmallest(self, root, k):
        # use binary serach interator to pop stack times and return the last node poped from the stack

        stack = []
        self.add_all_left_nodes(root, stack)

        for _ in range(k):
            # if stack is empty but not reach k times
            if not stack:
                return None

            node = stack.pop()
            if node.right:
                self.add_all_left_nodes(node.right, stack)

        return node.val

    def add_all_left_nodes(self, node, stack):
        while node:
            stack.append(node)
            node = node.left