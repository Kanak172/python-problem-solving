from collections import deque

class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        rows = len(mat)
        cols = len(mat[0])

        queue = deque()

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    queue.append((i,j))
                else:
                    mat[i][j] =-1

        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        while queue:
            row, col = queue.popleft()

            for dr,dc in directions:
                new_row = row + dr
                new_col = col + dc

                if (0 <= new_row < rows and 0 <= new_col < cols and mat[new_row][new_col] == -1):
                    mat[new_row][new_col] = mat[row][col] + 1
                    queue.append ((new_row, new_col))
        return mat