from collections import deque
class Solution:
    def isPalindrome(self, s: str) -> bool:
        #dq = deque()
        # for chars in s:
        #     if chars.isalnum():
        #         dq.appendleft(''.join(chars.lower()))
        dq = deque(''.join([chars for chars in s if chars.isalnum()]).lower())
        while len(dq) > 1:
            if dq.pop() != dq.popleft():
                return False
        return True
                