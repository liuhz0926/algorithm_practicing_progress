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
    @param target: the given target
    @param k: the given k
    @return: k values in the BST that are closest to the target
    """

    def closestKValues(self, root, target, k):
        # traverse 89 + 460的答案版本
        if not root or k == 0:
            return []

        order = self.get_traverse(root)
        right = self.find_upper_closest(order, target)
        left = right - 1

        result = []
        for _ in range(k):
            if self.is_left_closer(order, target, left, right):
                result.append(order[left])
                left -= 1
            else:
                result.append(order[right])
                right += 1

        return result

    def get_traverse(self, root):
        dummy = TreeNode(0)
        dummy.right = root
        stack = [dummy]
        order = []

        while stack:
            node = stack.pop()
            if node.right:
                n = node.right
                while n:
                    stack.append(n)
                    n = n.left
            if stack:  # can't add 0 dummy in, and we need to add the last largest element in
                order.append(stack[-1].val)

        return order

    def find_upper_closest(self, order, target):
        start, end = 0, len(order) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if order[mid] >= target:
                end = mid
            else:
                start = mid

        if order[start] >= target:
            return start
        if order[end] >= target:
            return end

        return len(order)

    def is_left_closer(self, order, target, left, right):
        if left < 0:
            return False
        if right >= len(order):
            return True

        return target - order[left] <= order[right] - target
