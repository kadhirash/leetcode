class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or int(s) < 0 or s[0]=='0':
            return 0
        dp = [0] * (len(s)+1)
        
        # base case initialization
        dp[0] = 1 
        if s[0] == "0":
            dp[1] = 0 
        else:
            dp[1] = 1   
        
        for i in range(2, len(s) + 1): 
            # One step jump
            if int(s[i-1:i]) != 0:   
                dp[i] = dp[i - 1]
            # Two step jump
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i - 2]
                
        return dp[-1]