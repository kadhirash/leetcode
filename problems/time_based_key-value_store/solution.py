import collections
from collections import defaultdict
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time_map = collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((value,timestamp))
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""
        
        timemap = self.time_map[key]
        i = len(timemap)-1
        
        while i >=0 and timemap[i][1] > timestamp:
            i -= 1
        if i >= 0:
            return timemap[i][0]
        else:
            return ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)