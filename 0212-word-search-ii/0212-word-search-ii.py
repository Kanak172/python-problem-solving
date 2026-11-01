class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None
class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:

        root =TrieNode()

        for word in words:
            node = root

            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()

                node = node.children[char]

            node.word = word

        rows = len(board)
        cols = len(board[0])
        result = []

        def dfs(r, c, node):
            char = board[r][c]

            if char not in node.children:
                return
            curr_node = node.children[char]

            if curr_node.word is not None:
                result.append(curr_node.word)
                curr_node.word = None

            board[r][c] = "#"

            for dr, dc in [(0,1), (0, -1), (1, 0), (-1, 0)]:
                nr = r + dr
                nc = c + dc

                if (0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#"):
                    dfs(nr, nc, curr_node)

            board[r][c] = char



        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return result


                
        