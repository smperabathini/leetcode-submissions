class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        zeros = [0] * (n-1)
        total = 0
        for i in range(0,n-1):
            if s[i] == '0':
                total += 1
                zeros[i] = total
        ones = [0] * (n-1)
        total = 0
        for i in range(n-1,0,-1):
            if s[i] == '1':
                total += 1
                ones[i-1] = total
        res = 0
        for i in range(n-1):
            res = max(res,zeros[i] + ones[i])
        return res


            
