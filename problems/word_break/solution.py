import collections
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # q/a:
            # if no s or no wordDict: return False
        # strat:
            # bfs 
                # deque
            # wordDict -> wordset 
            # visited 
            # pop off the s 
            # create new_string
                # == ''
                
        if not s or not wordDict:
            return False
        
        word_set = set(wordDict)
        visited = set()
        
        queue = collections.deque()
        queue.append(s)
        
        while queue:
            s = queue.popleft()
            
            for word in word_set:
                if s.startswith(word):
                    new_str = s[len(word):]
                    if new_str == '':
                        return True
                    elif new_str not in visited:
                        queue.append(new_str)
                        visited.add(new_str)
        return False