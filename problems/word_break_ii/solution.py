class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dp = {}
        def word_break(s):
            if s in dp: return dp[s]
            res = []
            for w in wordDict:
                if s[:len(w)] == w:
                    if len(w) == len(s):
                        res.append(w)
                    else:
                        temp = word_break(s[len(w):])
                        for t in temp:
                            res.append(w + " " + t)
            dp[s] = res
            return res
        return word_break(s)
    
