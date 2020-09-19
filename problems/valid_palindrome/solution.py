class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 2 pointers to compare the left to the right side
            # move the left side,right to the middle, and move right side, left to the middle
            # if they are both of lenght 0, return True, else return False
        
        
        if not s: 
            return True
        
        left, right = 0, len(s)-1
        
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            
            
            if s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True
            