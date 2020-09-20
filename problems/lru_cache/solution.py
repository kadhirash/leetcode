# DLL
class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def get(self, key: int) -> int: #refresh how new it was
        if key in self.dict:
            node = self.dict[key]
            self._remove(node)
            self._add(node)
            return node.value
        else:
            return -1
        
        

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self._remove(self.dict[key])
            del self.dict[key]
        elif len(self.dict) >= (self.capacity):
            node = self.head.next
            self._remove(node)
            del self.dict[node.key]
            
        # add item to the MRU side of LRU cache
        node = Node(key, value)
        self.dict[key] = node   
        self._add(node)
    
    def _remove(self,node): # remove node
        prev = node.prev
        prev.next = node.next
        node.next.prev = prev
    
    
    def _add(self, node): # add to tail for MRU side and pop from head for LRU side 
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node
        

    
        
    
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)