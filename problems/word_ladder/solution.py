import collections
import string
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # create word_set
        # visited set
        # queue -> beginWord, length
        # letters
        
        
        
        word_set = set(wordList)
        visited = set()
        
        queue = collections.deque()
        queue.append((beginWord,1))
        
        while queue:
            word,shortest_len = queue.popleft()
            size = len(word)
            
            if word == endWord:
                return shortest_len
            
            for i in range(size):
                for j in string.ascii_lowercase:
                    new_word = word[:i] + j + word[i+1:]
                    if new_word in word_set and new_word not in visited:
                        queue.append((new_word, shortest_len + 1))
                        visited.add(new_word)
        return 0