import collections
from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # edge cases
        if not beginWord or not endWord or not wordList:
            return None
        
        combinations = defaultdict(list)
        for words in wordList:
            for i in range(len(beginWord)):
                combinations[words[:i] + "#" + words[i+1:]].append(words)
        #print(combinations)
        
        #bfs
        queue = deque([(beginWord,1)])
        #print(queue) #(['hit', 1])
        visited = {beginWord: True}
        
        while queue:
            curr_word, level = queue.popleft()
            for i in range(len(beginWord)):
                middle_words = curr_word[:i] + "#" + curr_word[i+1:]
            #print(middle_words) #      hi#
        
                for words in combinations[middle_words]:
                    if words == endWord:
                        return level + 1
                    if words not in visited:
                        visited[words] = True
                        queue.append((words,level+1))
                combinations[middle_words] = []
    
        return 0