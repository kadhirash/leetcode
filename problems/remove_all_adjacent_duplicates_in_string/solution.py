class Solution:
    def removeDuplicates(self, S: str) -> str:
        ans = []
        for char in S:
            if ans and ans[-1] == char:
                ans.pop()
            else:
                ans.append(char)
        return ''.join(ans)