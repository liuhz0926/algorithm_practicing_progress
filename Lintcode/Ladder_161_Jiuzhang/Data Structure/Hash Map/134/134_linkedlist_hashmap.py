# 用linkedlist来解决
# 新节点从尾部加入，老节点从头部移走
# 这里如果大于capacity，我们就删除头结点，插入新的话，把它放在结尾
# 如果call get了一个在队列里的，把它放在队尾作为most recently
# 有一个hash 存hash[1] = dummy, hash[2] = node1
class LinkedNode:
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next


class LRUCache:
    """
    @param: capacity: An integer
    """

    def __init__(self, capacity):
        # 记录每一个点的前一个node
        # 因为我们需要连接这个key对应的current的前面和后面，所以我们就干脆村成了，key对应的前面，而key 对应的点无非就是prev.next
        self.key_to_prev = {}
        self.capacity = capacity
        self.dummy = LinkedNode()
        # 保证tail存在，目前是只有头dummy
        self.tail = self.dummy

    def push_back(self, node):  # 可以理解为插入一个点在结尾，也可以理解为把前面的放到结尾中的一步
        # 把这个node放在当前的tail的后面
        # 现在的tail还是以前的tail
        self.key_to_prev[node.key] = self.tail
        self.tail.next = node
        # 这个点成为tail
        self.tail = node

    def pop_front(self):
        # 删除头部
        head = self.dummy.next
        del self.key_to_prev[head.key]
        self.dummy.next = head.next
        self.key_to_prev[head.next.key] = self.dummy

    # 讲prev的下一位移动到尾部
    # change 'prev -> node -> next -> ... -> tail' to 'prev  -> next -> ... -> tail -> node'
    def kick(self, prev):
        # 这里虽然input是prev，但是我们想kick的是current也就是prev.next
        node = prev.next
        # 就在尾巴了
        if node == self.tail:
            return

            # remove the current node from linkedlist
        prev.next = node.next
        # update the previous node in hashmap
        self.key_to_prev[node.next.key] = prev
        node.next = None

        # 放在尾巴上
        self.push_back(node)

    """
    @param: key: An integer
    @return: An integer
    """

    def get(self, key):
        # 有没有这个key，没有 return -1
        if key not in self.key_to_prev:
            return -1

        # 找到这个key对应的node和node的prev
        prev = self.key_to_prev[key]
        current = prev.next

        # get后需要把current放在最后，
        # 注意我们写的kick是input prev而不是current！！
        self.kick(prev)
        return current.value

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """

    def set(self, key, value):
        # 如果这个key现在已经被占了：
        if key in self.key_to_prev:
            # 把当前这个点给放到最后，然后更新新的value
            self.kick(self.key_to_prev[key])
            # 注意我们kick后，keytoprev里key对应的prev已经变成以前的tail了，不一样了 (先后setup value都一样)
            self.key_to_prev[key].next.value = value
            # 这里因为没有插入一个新的，只是更改了旧的，所以就不用考虑有没有超capacity
            return

            # 插入一个新的, key不在，存入一个新的节点在结尾，因为是最recent提及的
        self.push_back(LinkedNode(key, value))
        # 如果缓存超出了上限
        if len(self.key_to_prev) > self.capacity:
            # 删除头部，最不经常用的
            self.pop_front()

