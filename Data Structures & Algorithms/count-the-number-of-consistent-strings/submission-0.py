class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res = 0
        hs = set()
        for char in allowed:
            hs.add(char)
        for word in words:
            add = True
            for char in word:
                if char not in hs:
                    add = False
                    break
            if add:
                res += 1
        return res
                