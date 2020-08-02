class LRUCache:

    def __init__(self, capacity: int):
        self.dic = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        value = self.dic[key]
        del self.dic[key]
        self.dic[key] = value
        #self.dic.move_to_end(key)
        return value
        

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            del self.dic[key]
        self.dic[key] = value
        if len(self.dic) > self.capacity:
            self.dic.popitem(last=False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)