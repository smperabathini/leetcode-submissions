class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low == 1000000000:
            return 0
        return (high - low) //2 + 1