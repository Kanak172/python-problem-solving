class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])

        dp = [[0]* cols for _ in range(rows)]
        dp[0][0] = grid[0][0]

        for i in range(rows):
            for j in range(cols):
                if i == 0 and j == 0 :
                        continue
                elif i == 0:
                    dp [i][j] = dp[i][j-1] + grid[i][j]
                elif j == 0:
                    dp[i][j] = dp[i-1][j] +grid[i][j]
                else:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j]) +grid[i][j]
        
        return dp[rows - 1][cols - 1]