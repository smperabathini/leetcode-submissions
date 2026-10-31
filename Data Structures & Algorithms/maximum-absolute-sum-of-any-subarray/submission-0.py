class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum = nums[0]
        cur_sum = 0

        for num in nums:
            cur_sum = max(cur_sum + num, num)
            max_sum  = max(cur_sum, max_sum)
        min_sum = nums[0]
        cur_min = 0
        for num in nums:
            cur_min = min(cur_min + num, num)
            min_sum = min(cur_min, min_sum)
        return max(abs(max_sum), abs(min_sum))


