from typing import List

class Solution:
    def __init__(self):
        self.m = 0
        self.n = 0

    def find_neighbor_loations(self, index):
        i = index[0]
        j = index[1]
        neighbor_locations = [(i-1, j-1), (i-1, j), (i-1, j+1),
                               (i, j-1), (i, j+1),
                               (i+1, j-1), (i+1, j), (i+1, j+1)]
        return neighbor_locations
    

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        result = board
        self.m = len(board)
        self.n = len(board[0])
        for i in range(self.m):
            for j in range(0,self.n):
                neighbor_locations = self.find_neighbor_loations((i,j))
                neighbor_values = []
                for loc in neighbor_locations:
                    if (loc[0] >= 0 and loc[0] < self.m) and (loc[1] >= 0 and loc[1] < self.n):
                        neighbor_value = board[loc[0]][loc[1]]
                        neighbor_values.append(neighbor_value)
                if sum(neighbor_values) < 2: result[i][j] = 0
                elif sum(neighbor_values) == 2 or sum(neighbor_values) == 3 : result[i][j] = 1
                elif sum(neighbor_values) > 3: result[i][j] = 0
                elif sum(neighbor_values) == 3 and board[i][j] == 0: result[i][j] = 1
                #print(neighbor_values)
        return result

if __name__ == '__main__':
    print(Solution().gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]])) # output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
    print(Solution().gameOfLife([[1,1],[1,1]])) # [[1,1],[1,0]