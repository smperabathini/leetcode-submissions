from collections import defaultdict
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        starts = set()
        ends = set()
        for start,end in paths:
            starts.add(start)
            ends.add(end)
        iterate = list(starts)
        for start in iterate:
            if start in ends:
                starts.remove(start)
                ends.remove(start)
        return ends.pop()
