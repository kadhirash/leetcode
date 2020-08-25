class Solution:

    def __init__(self, nums: List[int]):
        self.card_deck = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.card_deck

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        shuffled_deck = self.card_deck[:]
        random.shuffle(shuffled_deck)
        return shuffled_deck

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()


