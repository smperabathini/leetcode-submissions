class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total = 0
        for i in range(len(mat)):
            total += mat[i][i]
            total += mat[i][len(mat) - 1- i]
        if len(mat) % 2 == 1:
            total -= mat[len(mat) //2][len(mat)// 2]
        return total
        