class ListNode:
    def __init__(self, val=0, key=0, next=None, prev=None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = {}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        
        # move to head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head

        return self.cache[key].val
        

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            # print("new", key, value)
            node = ListNode(value, key)
            self.cache[key] = node

            self.size += 1

            
            # move to head
            node.next = self.head.next
            self.head.next.prev = node
            self.head.next = node
            node.prev = self.head

            # print("size", self.size, "capacity", self.capacity)
            if self.size > self.capacity:
                node = self.tail.prev
                # print("removing", node.key, node.val)
                self.tail.prev = node.prev
                if self.tail.prev:
                    self.tail.prev.next = self.tail
                del self.cache[node.key]
                self.size -= 1
        else:
            node = self.cache[key]
            node.val = value

            if node.prev:
                node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev

            # move to head
            node.next = self.head.next
            self.head.next.prev = node
            self.head.next = node
            node.prev = self.head


        
# WA ["LRUCache", [2], "put", [1, 1], "put", [2, 2], "get", [1], "put", [3, 3], "get", [2], "put", [4, 4], "get", [1], "get", [3], "get", [4]]
# ["LRUCache", [2], "put", [1, 10],  "get", [1], "put", [2, 20], "put", [3, 30], "get", [2], "get", [1]]
# 