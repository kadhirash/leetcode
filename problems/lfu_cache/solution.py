


# use DLL + Dictionary

# DLL
    # LLNode
# Dictionary

# LRUCache
    # get
        # if key exists, get value
        # if no key, return -1
    # put
        # if key exists but not in cache:
            # set/insert value
        # when cache reaches capacity
            # invalidate lfu item BEFORE inserting new item
        # if tie (2 or more items with same freq.), lru key popped
    # # of times item used = # of calls to get/put functions
    # number set to 0 when item removed
class LLNode:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None
        
class DLL:
    def __init__(self):
        self.head = LLNode(0, 0)
        self.tail = LLNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
        
    def insertHead(self, node):
        headNext = self.head.next
        headNext.prev = node
        self.head.next = node
        node.prev = self.head
        node.next = headNext
        self.size += 1
        
    def removeNode(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
        self.size -= 1
        
    def removeTail(self):
        tail = self.tail.prev
        self.removeNode(tail)
        return tail
    
class LFUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.freq_table = collections.defaultdict(DLL)
        self.capacity = capacity
        self.min_freq = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        return self.maintainCache(self.cache[key], key, self.cache[key].val)

    def put(self, key: int, value: int) -> None:
        # if nothing in capacity
        if not self.capacity:
            return
        # set or insert value if key is not present
        if key in self.cache:
            self.maintainCache(self.cache[key], key, value)
        else:
            # when cache reaches capacity
            if len(self.cache) == self.capacity:
                prev_tail = self.freq_table[self.min_freq].removeTail()
                del self.cache[prev_tail.key]
            node = LLNode(key, value)
            self.freq_table[1].insertHead(node)
            self.cache[key] = node
            self.min_freq = 1
            
    def maintainCache(self,node:LLNode,key: int,value: int) -> int:
            node = self.cache[key]
            node.val = value
            prev_freq = node.freq
            node.freq += 1
            self.freq_table[prev_freq].removeNode(node)
            self.freq_table[node.freq].insertHead(node)
            if prev_freq == self.min_freq and self.freq_table[prev_freq].size == 0:
                self.min_freq += 1
            return node.val
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)