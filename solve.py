from typing import List

class Solution:
        
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board: return board
        m, n = len(board), len(board[0])
        directions = {
            "up": (0, -1),
            "left": (-1, 0),
            "right": (1, 0),
            "down": (0, 1),
        }
        visited = set()
        flip = set()

        def cell_on_border(i, j):
            return (i == 0) or (i == m-1) or (j == 0) or (j == n-1)
        
        def dfs(i, j):
            if (i < 0) or (i >= m) or (j < 0) or (j >= n) or board[i][j] != 'O':
                return
            board[i][j] = 'T'
            dfs(i, j-1)
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j+1)
            
        # Iterate rows
        for i in range(m):
            # Iterate columns
            for j in range(n):
                # Check if cell on border, continue
                if cell_on_border(i, j): dfs(i, j)

        for i in range(m):
            # Iterate columns
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

        for i in range(m):
            # Iterate columns
            for j in range(n):
                if board[i][j] == 'T':
                    board[i][j] = 'O'

        return board
    
if __name__ == "__main__":
    print(Solution().solve(board = [["X"]])) # [["X"]]
    print(Solution().solve(board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])) # [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
    print(Solution().solve(board = [["O","O","O"],["O","O","O"],["O","O","O"]])) # [["O","O","O"],["O","X","O"],["O","O","O"]]