import collections
import string
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # ex:
            # beginWord: 'hit'
            # endWord: 'cog'
            # wordList:  ["hot","dot","dog","lot","log","cog"] # 4 iterations, length = 5
        # qa:
            # endWord in wordList
            # no duplicates in wordList
            # return 0 if no formation
            # all lowercase
        # strat:
            # BFS
                # queue
            
        word_set = set(wordList)
        visited = set()
        
        queue = collections.deque()
        queue.append((beginWord,1)) # beginWord, length
        
        while queue:
            word,length = queue.popleft()
            
            if word == endWord:
                return length
            
            for i in range(len(word)):
                for j in string.ascii_lowercase:
                    new_word = word[:i] + j + word[i+1:]
                    if new_word not in visited and new_word in word_set:
                        queue.append((new_word, length + 1))
                        visited.add(new_word)
        return 0