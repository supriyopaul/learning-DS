from typing import List

class Solution:

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        board_copy = board.copy()
        directions = [(-1, -1), (-1,0), (-1,1), (0,-1), (0,1), (1, -1), (1,0), (1,1)]
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                live_cells = 0
            for direction in directions:
                ni, nj = direction[0] + i, direction[1] + j
                if (0 <= ni < m) and (0 <= nj < n) and board_copy[ni][nj] == 1:
                    live_cells += 1
            print(live_cells)
            if board_copy[i][j] == 1 and (live_cells < 2 or live_cells > 3):
                board[i][j] = 0
            elif board_copy[i][j] == 0 and live_cells == 3:
                board[i][j] = 1
        return board

if __name__ == '__main__':
    print(Solution().gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]])) # output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
    print(Solution().gameOfLife([[1,1],[1,1]])) # [[1,1],[1,0]