class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # non empty string = s
        # non empty words = wordDict
        # can s be made from wordDict
        
        # same word from wordDict can be used
        # dictionary = no duplicates
        
        # queue to put string in 
        # set so no duplices
        # iterate through queue and pop off values and set it to the string
            # compare words in wordDict to the queue
            # make a new string = s[len(word):]
            # if true, new_string and add to seen
            # if in seen -> return True, else False
            
        
        queue = [s]
        seen = set()
        while queue:
            s = queue.pop()
            for word in wordDict:
                if s.startswith(word):
                    new_string = s[len(word):]
                    if new_string == "":
                        return True
                    if new_string not in seen:
                        queue.append(new_string)
                        seen.add(new_string)
        return False
        