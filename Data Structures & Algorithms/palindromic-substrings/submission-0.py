class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        def expand(l, r):
            nonlocal count
            while l > -1 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
        for i in range(0, len(s) -1):
            expand(i,i)
            expand(i,i+1)
        expand(len(s) - 1, len(s) - 1)
        return count

