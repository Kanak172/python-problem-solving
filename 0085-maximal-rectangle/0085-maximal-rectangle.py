class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0 

        rows = len(matrix)
        cols = len(matrix[0])
        heights = [0] * (cols + 1)
        max_area = 0

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == "1":
                    heights[c] += 1
                else:
                    heights[c] = 0

            stack = []

            for i in range(cols + 1):
                while stack and heights[stack[-1]] > heights[i]:
                    height = heights[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, height * width) 

                stack.append(i)

        return max_area
        