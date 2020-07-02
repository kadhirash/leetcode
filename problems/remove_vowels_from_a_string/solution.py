class Solution:
    def removeVowels(self, S: str) -> str:
        for i in S:
            if i in 'aeiou':
                S = S.replace(i,'')
        return S