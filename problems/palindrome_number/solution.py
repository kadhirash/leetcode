class Solution:
    def isPalindrome(self, x: int) -> bool:
        # todo
            # return true if number is palindrome
        # ex:
            # 121
            # True 
        # strat:
            # reverse half the number 
            # if x < 0: False
            # pal = x
                # while pal:
                    # 121 % 10 --> 1 
                    # 121 // 10 -> 12
        
        
    
        pal = x
        pop = 0
        
        
        if x < 0: return False
        if x >= 0 and x < 10: return True
        
        
        while pal:
            pop = pop * 10 + pal % 10     # 1     ->  12   -> 121
            
            pal //= 10                    # 12    -> 1
    
        return pop == x
        
        