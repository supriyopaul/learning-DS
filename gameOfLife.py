from typing import List
import copy

class Solution:

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        board_copy = copy.deepcopy(board)
        n = len(board_copy[0])
        m = len(board_copy)
        print(m, n)
        #import pdb; pdb.set_trace()
        directions = [[-1,-1], [-1,0], [-1,1], [0,-1], [0,1], [1,-1], [1,0], [1,1]]
        live_neighbors = {}
        for column in range(m):
            for row in range(n):
                if (column,row) not in live_neighbors:  live_neighbors[(column,row)] = 0
                for direction in directions:
                    neighbor_location = column+direction[0], row+direction[1]
                    if 0 <= neighbor_location[0] < m and 0 <= neighbor_location[1] < n:
                        print(neighbor_location)
                        if board_copy[column+direction[0]][row+direction[1]] == 1:
                            live_neighbors[(column,row)] += 1
        print(live_neighbors)
        for location, live_neighbor_count in live_neighbors.items():
            if live_neighbor_count < 2: board[location[0]][location[1]] = 0
            if 2 <= live_neighbor_count <= 3 and board_copy[location[0]][location[1]] == 1: board[location[0]][location[1]] == 1
            if live_neighbor_count > 2: board[location[0]][location[1]] = 0
            if live_neighbor_count == 3: board[location[0]][location[1]] = 1
        return board

if __name__ == '__main__':
    print(Solution().gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]])) # output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
    print(Solution().gameOfLife([[1,1],[1,1]])) # [[1,1],[1,0]