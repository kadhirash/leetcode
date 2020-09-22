class Solution:
    def firstUniqChar(self, s: str) -> int:
        # using a hashmap to keep track of indexes
        
        ans = {}
        
        for count, letter in enumerate(s):
            
            if letter not in ans:
                ans[letter]= 1
            else:
                ans[letter] += 1
                
        for letter in ans:
            if ans[letter] == 1:
                return s.index(letter)
        return -1
        