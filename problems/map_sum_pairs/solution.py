class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}

    def insert(self, key: str, val: int) -> None:
        self.dict[key] = val

    def sum(self, prefix: str) -> int:
        return sum(self.dict[i] for i in self.dict if i.startswith(prefix))
    
        count = 0
        for i in self.dict:
            if i.startswith(prefix):
                count += 1
        return count
    

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)