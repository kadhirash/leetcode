import collections
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # bfs using queue 
            # deque 
        
        word_set = set(wordDict)
        visited = set()
        
        queue = collections.deque()
        queue.append(s)
        
        while queue:
            s_1 = queue.popleft()
            
            for word in word_set:
                if s_1.startswith(word):
                    new_str = s_1[len(word):]
                    if new_str == '':
                        return True
                    elif new_str not in visited:
                        queue.append(new_str)
                        visited.add(new_str)
        return False