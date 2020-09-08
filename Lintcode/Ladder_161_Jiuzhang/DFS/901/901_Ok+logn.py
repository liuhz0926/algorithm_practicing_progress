class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @param k: the given k
    @return: k values in the BST that are closest to the target
    """

    def closestKValues(self, root, target, k):
        if root is None or k == 0:
            return []

        lower_stack = self.get_stack(root, target)
        # hard copy lower stack
        upper_stack = list(lower_stack)
        # 让upperstack里面contains upper closest
        # 让lowerstack里面contains lower closest
        if lower_stack[-1].val < target:
            self.move_upper(upper_stack)
        else:
            self.move_lower(lower_stack)

        # 然后开始找k个closest node
        result = []
        for i in range(k):
            if self.is_lower_closer(lower_stack, upper_stack, target):
                # lower closer 的话把lower头加进去。然后去找比这个头小一位的做新的头
                result.append(lower_stack[-1].val)
                self.move_lower(lower_stack)
            else:
                # upper closer的话把upper头加进去，然后去找比这个头大一位做新的头
                result.append(upper_stack[-1].val)
                self.move_upper(upper_stack)

        return result

    def get_stack(self, root, target):
        '''
        像插入target到树里面一样。把一路经过的node全部放入stack里面
        :param root:
        :param target:
        :return:
        '''
        stack = []
        while root:
            stack.append(root)
            if target < root.val:
                root = root.left
            else:
                root = root.right

        return stack

    def move_lower(self, stack):
        '''
        ！！！这里是去找现在原本的bst里面比stack头小一位的那个node
        最开始第一次call的地方：
            如果 stack 的头是大于target的话：
            我们要找 比target小的那个临界值。

            这个头如果有left,有比他小的，则把他的left的靠右的一行
            这些都要比这个头小，然后最右边的最下面的leaf 是比现在这个头要稍微小一点的点。
            也就是说这个值可能是和原来的头 把target加在中间

            否则，因为右边都比他大，所以我们要把这个头pop出去，如果pop出来的点和现在stack 头是，头的left是pop出去的（
                说明前面这个新的头比pop出去的大，所以我们要找小的那个。所以要继续pop，

            找到如果是 头的right 是pop出去的，就对了

            保证stack 头是lower的临界值
        :param stack:
        :return:
        '''
        if stack[-1].left:
            node = stack[-1].left
            while node:
                stack.append(node)
                node = node.right
        else:
            node = stack.pop()
            while stack and stack[-1].left == node:
                node = stack.pop()

    def move_upper(self, stack):
        '''
        ！！！这里是去找现在原本的bst里面比stack头大一位的那个node
        最开始第一次call的地方：
            如果stack的头是小于target的话：我们要找比target大的那个临界值

            头有right，所以找到这个right child 的最左。就是头《target《最左

            头没有right，那就pop出来看前面这个node，前面这个node如果他的右是pop（说明这个node小，不对。继续pop
            要找到刚好stack是剩下的头为第一个这个头的left是pop出去的

            保证stack 头是upper的临界值
        :param stack:
        :return:
        '''
        if stack[-1].right:
            node = stack[-1].right
            while node:
                stack.append(node)
                node = node.left
        else:
            node = stack.pop()
            while stack and stack[-1].right == node:
                node = stack.pop()

    def is_lower_closer(self, lower_stack, upper_stack, target):
        '''
        检查是lower closer 还是 upper 的stack closer
        :param lower_stack:
        :param upper_stack:
        :param target:
        :return:
        '''
        # lower空
        if not lower_stack:
            return False

        # upper空
        if not upper_stack:
            return True

        # lower头 的差小还是大
        return target - lower_stack[-1].val < upper_stack[-1].val - target