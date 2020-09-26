import random
class Solution:

    def __init__(self, nums: List[int]):
        self.card_deck = nums
        self.og = list(nums)

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.card_deck = self.og
        self.og = list(self.og)
        return self.card_deck

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        for i in range(len(self.card_deck)):
            swap_i = random.randrange(i, len(self.card_deck))
            self.card_deck[i] , self.card_deck[swap_i] = self.card_deck[swap_i], self.card_deck[i]
        return self.card_deck

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()


