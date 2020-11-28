class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        lenw = len(words)
        if not words: return False
        try:
            for i in range(lenw):
                lenj = len(words[i])
                for j in range(lenj):
                    if words[i][j] != words[j][i]:
                        return False
            return True
        except:
            return False
            