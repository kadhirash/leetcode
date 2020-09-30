class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self,capacity):
        self.capacity = capacity
        self.dict = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def add(self,node): 
        p = self.tail.prev
        p.next = node
        node.next = self.tail
        
        node.prev = p
        self.tail.prev = node
        
        
    def remove(self,node):   # LRU side, p (0,0)    (node)      (0,0) tail on MRU side
        p = node.prev
        p.next = node.next
        node.next.prev = p
        
    def get(self, key):
        if not key in self.dict:
            return -1
        node = self.dict[key]
        self.remove(node)
        self.add(node)
        return node.value
    
    def put(self,key,value):
        # remove
        if key in self.dict:
            self.remove(self.dict[key]) # del from list
            del self.dict[key] # del from dict
        elif len(self.dict) >= self.capacity:
            node = self.head.next
            self.remove(node) # del from list
            del self.dict[node.key] # del from dict
        
        # add to MRU side
        node = Node(key,value)
        self.add(node)
        self.dict[key] = node
        
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)