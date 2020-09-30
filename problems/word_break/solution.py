import collections
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # q/a 
            # return false if empty string
            
        # strat:
            # BFS via queue
            
        
        word_set = set(wordDict)
        visited = set()
        
        queue = collections.deque()
        queue.append(s)
        
        while queue:
            new_str = queue.popleft()
            
            for i in word_set:
                if new_str.startswith(i):
                    substr = new_str[len(i):]
                    if substr == "":
                        return True
                    elif substr not in visited:
                        queue.append(substr)
                        visited.add(substr)
        return False