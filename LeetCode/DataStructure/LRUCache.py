class Node:
    def __init__(self, value=0, key=0):
        self.pre = None
        self.next = None
        self.value = value
        self.key = key


class LRUCache(object):
    def __init__(self, capacity):
        self.mp = {}
        self.tail = None
        self.head = None
        self.capacity = capacity
        self.count = 0

    def insert_at_head(self, node):
        if self.count == 0:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.pre = node
            self.head = node
        self.count += 1
        self.mp[node.key] = node

    def erase_at_tail(self):
        if self.count == 0:
            return
        n_node = self.tail
        if self.count == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = n_node.pre
            self.tail.next = None
        n_node.pre = None
        n_node.next = None
        n_key = n_node.key
        self.mp.pop(n_key)
        self.count -= 1

    def get(self, key):
        if key not in self.mp:
            return -1
        n_node = self.mp[key]
        if n_node == self.head:
            return n_node.value
        pre_node = n_node.pre
        next_node = n_node.next
        if n_node == self.tail:
            self.erase_at_tail()
        else:
            pre_node.next = next_node
            next_node.pre = pre_node
            n_node.pre = None
            n_node.next = None
            n_key = n_node.key
            self.mp.pop(n_key)
            self.count -= 1
        self.insert_at_head(n_node)
        return n_node.value

    def put(self, key, value):
        if self.get(key) != -1:
            self.head.value = value
            return
        if self.count == self.capacity:
            self.erase_at_tail()
        n_node = Node(value, key)
        self.insert_at_head(n_node)
