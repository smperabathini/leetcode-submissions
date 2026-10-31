class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        pointer = len(heights) - 1
        res = []
        prev = 0
        while pointer > -1:
            if heights[pointer] > prev:
                res.append(pointer)
                prev = heights[pointer]
            pointer -= 1
        return sorted(res)
