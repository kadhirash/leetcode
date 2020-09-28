# DLL + hashmap 
        # look up in O(1)
# add them in O(1)  

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
        
    def add(self,node):
        p = self.tail.prev
        p.next = node
        node.next = self.tail
        node.prev = p
        self.tail.prev = node

    def remove(self,node):
        p = node.prev
        p.next = node.next
        node.next.prev = p 

    def get(self, key: int) -> int:
        if not key in self.dict:
            return -1
        else:
            node = self.dict[key]
            self.remove(node)
            self.add(node)
            return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.remove(self.dict[key]) # remove from list
            del self.dict[key] # remove from hashmap
            
        elif len(self.dict) >= self.capacity:
            node = self.head.next
            self.remove(node)
            del self.dict[node.key]
        
        # ADD to the MRU
        node = Node(key,value)
        self.add(node) # add to lsit
        self.dict[key] = node # update the key value pairing in hashmap
    

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)