class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        ans = balance = 0
        
        for bracket in S:
            if bracket == '(':
                balance += 1
            else:
                balance -= 1
            if balance == -1: # if the balance is off 
                ans += 1  # incr ans 
                balance += 1  # inc bal
        return ans + balance # 