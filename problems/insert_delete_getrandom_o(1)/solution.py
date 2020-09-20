class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # hashmap + list
        self.dict = {}
        self.list = []

    def insert(self, x: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if x in self.dict:
            return False
        else:
            self.dict[x] = len(self.list)
            self.list.append(x)
            return True

    def remove(self, x: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if x in self.dict:
            last_elem = self.list[-1]
            curr_index = self.dict[x] 
            
            self.list[curr_index] = last_elem
            self.dict[last_elem] = curr_index
            
            self.list.pop()
            del self.dict[x]

            return True
        return False
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()