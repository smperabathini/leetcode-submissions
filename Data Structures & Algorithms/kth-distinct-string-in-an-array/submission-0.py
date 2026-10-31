class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        hm = defaultdict(int)
        for string in arr:
            hm[string] += 1
        for string in arr:
            if hm[string] == 1:
                k -=1
            if k == 0:
                return string
        return ""