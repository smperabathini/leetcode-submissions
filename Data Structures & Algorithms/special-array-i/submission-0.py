class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        cur = nums[0]
        for i in range(1, len(nums)):
            if nums[i] % 2 == cur %2:
                return False
            cur = nums[i]
        return True