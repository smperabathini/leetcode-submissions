class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        greatest = 1
        increasing = True
        curr = 1
        for i in range(len(nums) -1):
            if nums[i] == nums[i+1]:
                curr = 1
            elif increasing and nums[i+1] > nums[i]:
                curr += 1
                greatest = max(greatest,curr)
            elif not increasing and nums[i+1] < nums[i]:
                curr += 1
                greatest = max(greatest,curr)
            else:
                curr = 2
                increasing = not increasing
        return greatest
