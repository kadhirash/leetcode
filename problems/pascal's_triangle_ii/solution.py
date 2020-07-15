class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        facts = [1]
        for i in range(1, rowIndex+1):
            facts.append(facts[i-1]*i)
        
        def combination(n, k):
            return facts[n] // facts[k] // facts[n-k]
        
        ans = []
        for i in range(0, rowIndex+1):
            ans.append(combination(rowIndex, i))
        
        return ans