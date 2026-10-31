class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hm = defaultdict(int)
        for c in text:
            hm[c] +=1
        count = 0
        sent = True
        while sent:
            if hm['b'] >= 1 and hm['a'] >= 1 and hm['l'] >= 2 and hm['o'] >=2 and hm['n'] >=1:
                count += 1
                hm['b'] -= 1
                hm['a'] -= 1
                hm['l'] -= 2 
                hm['o'] -=2 
                hm['n'] -=1
            else:
                sent = False
        return count
