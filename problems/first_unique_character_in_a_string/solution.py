class Solution:
    def firstUniqChar(self, s: str) -> int:
        # only lowercase letters
        
        
        #strat:
            # use a hashmap to keep track of the indexes 
            # iterate through chars of s
                # add it to the hashmap
                    # if the value is !=0, return the first occurence
            
        # example:
            #"leetcode"
                # l: 0
                # e: 2
                # t: 0
                # c: 0
                # o : 0
                # d : 0
        ans = {} 
        
        for char in s:
            if char not in ans:
                ans[char] = 1
            else:
                ans[char] += 1
                
        
        for char in ans:
            if ans[char] == 1:
                return s.index(char)
        return -1