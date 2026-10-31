class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = [0] * len(nums)
        right = [0] * len(nums)
        curr = nums[0]
        for i in range(len(nums) - 1):
            left[i+1] = curr
            curr += nums[i+1]
        curr = nums[len(nums) - 1]
        for i in range(len(nums) -1, 0, -1):
            right[i - 1] = curr
            curr += nums[i-1]
        res = 0
        for i in range(len(nums)):
            if left[i] == right[i]:
                return i
        return -1