class MyHashSet:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key_val = 1013
        self.buckets = [[] for _ in  range(self.key_val)]
        
        
    def add(self, key: int) -> None:
        bucket, bucket_index = self._index(key)
        if bucket_index >= 0:
            return
        bucket.append(key)

    def remove(self, key: int) -> None:
        bucket, bucket_index = self._index(key)
        if bucket_index < 0:
            return
        bucket.remove(key)
        
    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        _, bucket_index = self._index(key)
        
        return bucket_index >= 0
         
    def _hash(self, key):
        return key % self.key_val
    
    def _index(self,key):
        hash = self._hash(key)
        bucket = self.buckets[hash]
        for i, k in enumerate(bucket):
            if k == key:
                return bucket, i
        return bucket, -1
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)