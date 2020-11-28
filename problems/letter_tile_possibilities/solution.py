class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        res = set()
        
        def dfs(path, t):
            tiles_len = len(t)
            if path not in res:
                if path:
                    res.add(path)
                for i in range(tiles_len):
                    dfs(path+t[i], t[i+1:] + t[:i])
                
        dfs('', tiles)
        return len(res)
    
    
   