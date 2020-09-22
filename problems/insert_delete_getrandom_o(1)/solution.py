class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashmap = {} #hashmap
        self.list = [] #list
            
    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        # check if val needs to be inserted 
            # return False
        # inserting values to hashmap/ list
        
        if val in self.hashmap:
            return False
        self.hashmap[val] = len(self.list)
        self.list.append(val)
        return True
    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """ 
        # O(1) --> list --> pop from end
            # swap index of val <--> last_elem
            
        if val in self.hashmap:
            last_elem = self.list[-1]
            index = self.hashmap[val]

            self.list[index] = last_elem
            self.hashmap[last_elem] = index

            self.list.pop()
            del self.hashmap[val]
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()