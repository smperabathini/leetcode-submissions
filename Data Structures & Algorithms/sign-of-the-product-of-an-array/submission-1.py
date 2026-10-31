class Solution:
    def arraySign(self, nums: List[int]) -> int:
        total = 1
        for num in nums:
            total *= num
        if total == 0:
            return 0
        return 1 if total > 0 else -1
