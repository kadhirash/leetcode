import re
from collections import Counter
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        ans = re.findall(r'\w+', paragraph.lower())
        counter = Counter(ans)
        for value, count in counter.most_common():
            if value not in banned:
                return value