class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet =set(wordDict)
        @functools.lru_cache
        def dfs(start: int):
            if start == len(s):
                return [[]]
            res = []
            for i in range(start, len(s)):
                if s[start:i+1] in wordSet:
                    res += [[s[start:i+1]] + child for child in dfs(i+1)]
            return res
        return [" ".join(line) for line in dfs(0)]
    
