class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        if len(nums) == 0:
            return [[]]
        arr = self.permute(nums[1:])
        for perm in arr:
            for i in range(0, len(perm) + 1):
                temp = perm.copy()
                temp.insert(i,nums[0])
                res.append(temp)
        return res