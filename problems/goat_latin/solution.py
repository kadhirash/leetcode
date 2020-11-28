class Solution:
    def toGoatLatin(self, S: str) -> str:
        def proc(idx, word):
            if word[0] not in 'aeiouAEIOU':
                word = word[1:] + word[0]

            return word + 'ma' + ('a' * idx)

        return ' '.join([proc(i, w) for i, w in enumerate(S.split(), 1)])