class Solution:
    def rob(self, nums: List[int]) -> int:
        with_alert, without_alert = 0,0
        for i in nums:
            with_alert, without_alert = without_alert + i, max(with_alert,without_alert)
        return max(without_alert,with_alert)
        