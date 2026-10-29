class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        n = len(mat)
        total = 0

        for i in range(n):
            total += mat[i][i]
            total += mat[i][n-1-i]

            if i == n - 1 - i:
                total -= mat[i][i]
        return total