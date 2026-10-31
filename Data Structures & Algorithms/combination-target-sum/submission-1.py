class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []
        def dfs(total, index):
            if total >= target:
                if total == target:
                    res.append(cur.copy())
                return
            for i in range(index,len(nums)):
                    cur.append(nums[i])
                    dfs(total+nums[i],i)
                    cur.pop()
        dfs(0,0)
        return res
            
            
            