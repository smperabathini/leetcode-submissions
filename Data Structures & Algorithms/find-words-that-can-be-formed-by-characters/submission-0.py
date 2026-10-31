class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        hs = defaultdict(int)
        for char in chars:
            hs[char] += 1
        res = 0
        for word in words:
            temp = hs.copy()
            add = True
            for char in word:
                if temp[char] > 0:
                    temp[char] -= 1
                else:
                    add = False
                    break
            if add:
                res += len(word)
        return res
            