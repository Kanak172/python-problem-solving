class Solution {
public:
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {
        int oldColor = image[sr][sc];
        
        // Edge case: If the starting pixel already has the target color, no change is needed
        if (oldColor == color) {
            return image;
        }

        int m = image.size();
        int n = image[0].size();
        
        queue<pair<int, int>> q;
        q.push({sr, sc});
        image[sr][sc] = color; // Paint the starting pixel immediately

        // Direction arrays for moving Up, Down, Left, Right
        int dRow[] = {-1, 1, 0, 0};
        int dCol[] = {0, 0, -1, 1};

        while (!q.empty()) {
            auto [r, c] = q.front();
            q.pop();

            // Check all 4 adjacent neighbors
            for (int i = 0; i < 4; i++) {
                int nextRow = r + dRow[i];
                int nextCol = c + dCol[i];

                // Validate boundaries and check if the neighbor matches the old color
                if (nextRow >= 0 && nextRow < m && nextCol >= 0 && nextCol < n && image[nextRow][nextCol] == oldColor) {
                    image[nextRow][nextCol] = color; // Paint it
                    q.push({nextRow, nextCol});       // Push to queue for further exploration
                }
            }
        }

        return image;
    }
};