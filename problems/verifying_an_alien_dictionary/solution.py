class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # use English lowercase letters, but can be diff. order
        # order = permutation of lowercase letters
        # return true iff words are sorted lexicographically
        
        
        
        # order --> order_map
        # order_map[c] = index in order
        
        order_map = {c: i for i,c in enumerate(order)} #gives key -> char 'c', value->index    of words AND order
        
        #print(order_map)
        
        # collect indices of all words and turn them into lists
        
        word_indices = [[(order_map[c]) for c in word] for word in words]
        #print(word_indices) # [[0, 6, 1, 1, 14], [1, 6, 6, 19, 4, 14, 5, 6]] b/c index position of words IN order
            
        # compare ALL words
        # The all() method returns True when all elements in the given iterable are true. If not, it returns False
        # zip() creates a tuple out of the iterables
        
        #print(word_indices)
        #print(word_indices[1:])
        #print (all(word_one <= word_other for word_one, word_other in zip(word_indices, word_indices[1:])))
        return all(word_one <= word_two for word_one, word_two in zip(word_indices, word_indices[1:]))