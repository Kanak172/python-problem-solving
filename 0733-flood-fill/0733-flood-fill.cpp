class Solution {
private:
    void dfs(vector<vector<int>>& image, int r, int c, int oldColor, int newColor) {
        // Boundary check and color match check
        if (r < 0 || c < 0 || r >= image.size() || c >= image[0].size() || image[r][c] != oldColor) {
            return;
        }

        // Change the current pixel's color
        image[r][c] = newColor;

        // Recursively visit all 4 directions (up, down, left, right)
        dfs(image, r - 1, c, oldColor, newColor);
        dfs(image, r + 1, c, oldColor, newColor);
        dfs(image, r, c - 1, oldColor, newColor);
        dfs(image, r, c + 1, oldColor, newColor);
    }

public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {
        int m = image.size();
        int n = image[0].size();
        int oldColor = image[sr][sc];

        // If the old color matches the target color, no change is needed (prevents infinite recursion)
        if (oldColor != color) {
            dfs(image, sr, sc, oldColor, color);
        }

        return image;
    }
};