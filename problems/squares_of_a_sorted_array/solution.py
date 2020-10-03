class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        if not A:
            return None
        return sorted([ i*i for i in A])