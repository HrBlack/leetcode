# LRU的思想是维护一个固定大小c的双向链表作为cache，把最近访问过的c个值存进去
# 要求O（1）复杂度
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

# 新的结点从链表的末尾增加
class LRUCache:
    def __init__(self, capacity: int):
        self.head, self.tail = Node(0, 0), Node(0, 0)    
        self.capacity = capacity
        self.dict = {}
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, key: int) -> int:
		# 如果key已经存过了，那么把原有的从链表中删除，新的从链表尾部加入
        if key in self.dict.keys():
            node = self.dict[key]
            self._remove(node)
            self._add(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict.keys():
            self._remove(self.dict[key])
        node = Node(key, value)
        self.dict[key] = node
        self._add(node)
        if len(self.dict) > self.capacity:
            node_remove = self.head.next
            self._remove(node_remove)
            del self.dict[node_remove.key]
        
    def _remove(self, node):
        memo = node
        p = node.prev
        n = node.next
        p.next, n.prev = n, p
    
    def _add(self, node):
        p = self.tail.prev  # tail is None，p就是最后一个node
        p.next, node.prev = node, p
        node.next, self.tail.prev = self.tail, node
        
