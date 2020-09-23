import collections
import string
class Solution:
    # string1 = "ABBK"
    # string2 = "DBCN"
    # dictionary = {"DBPN", "ABPN", "ABKK", "ABPN", "DCCN", "ABPK" }
    def ladderLength(self, string1: str, string2: str, dictionary: List[str]) -> int:
        word_set = set(dictionary)
        visited = set()
        queue = collections.deque([(string1,1)]) # string1, length
        alpha = string.ascii_lowercase
        
        while queue:
            word,length = queue.popleft()
            size = len(word)
            
            if word == string2:
                return length
            
            for i in range(size):
                
                for char in alpha:
                    
                    new_word = word[:i] + char + word[i+1:]
                    
                    if new_word in word_set and new_word not in visited:
                        
                        queue.append((new_word,length+1))
                        visited.add(new_word)
        return 0
        
        # O(n * 26* m) 
            # n = words
            # m = len(word)
        # O(n)