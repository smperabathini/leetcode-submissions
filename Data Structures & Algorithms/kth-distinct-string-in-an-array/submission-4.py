class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        hs = set()
        duplicates = set()
        for s in arr:
            if s in hs:
                hs.remove(s)
                duplicates.add(s)
            if s not in duplicates:
                hs.add(s)
        for s in arr:
            if s in hs:
                k -= 1
                if k == 0:
                    return s
        return ""
        


            
        