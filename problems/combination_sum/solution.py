class Solution:
    
    def dfs(self, remain, combo, index):
        if remain == 0:
            self.ans.append(combo)
    
        for i in range(index,len(self.sorted_candidates)):
            if self.sorted_candidates[i] > remain:
                break # since sum >
            self.dfs(remain - self.sorted_candidates[i], combo +[self.sorted_candidates[i]], i)
            
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.sorted_candidates = sorted(candidates)
        self.ans = []
        self.dfs(target,[],0) # remain,combo,index
        return self.ans
    
    