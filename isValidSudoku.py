from typing import List

class Solution:
    def _check_grid_value(self, value, grid_num):
        if value in self.grid_values[grid_num]: return False
        else:
            self.grid_values[grid_num].add(value)
            return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        row -> 0,1,2..8
        column -> 0,1,2..8
        grid -> 0,1,2..8
        '''
        row_values = {num: set() for num in range(0, 9)}
        column_values = {num: set() for num in range(0, 9)}
        self.grid_values = {num: set() for num in range(0, 9)}

        for row in range(len(board)):
            for column in range(len(board[row])):
                #print(f"Row: {row}")
                #print(f"Column: {column}")
                if board[row][column] == ".": continue
                if board[row][column] in row_values[row] or board[row][column] in column_values[column]:
                    return False
                row_values[row].add(board[row][column])
                column_values[column].add(board[row][column])

                if column <= 2 and row <= 2:
                    #print(f"Grid: 1")
                    if not self._check_grid_value(board[row][column],0): return False
                elif 3 <= column <=5 and row <= 2:
                    #print(f"Grid: 2")
                    if not self._check_grid_value(board[row][column],1): return False
                elif 6 <= column <=8 and row <= 2:
                    #print(f"Grid: 3")
                    if not self._check_grid_value(board[row][column],2): return False
                
                elif column <= 2 and 3 <= row <=5:
                    #print(f"Grid: 4")
                    if not self._check_grid_value(board[row][column],3): return False
                elif 3 <= column <=5 and 3 <= row <=5:
                    #print(f"Grid: 5")
                    if not self._check_grid_value(board[row][column],4): return False
                elif 6 <= column <=8 and 3 <= row <=5:
                    #print(f"Grid: 6")
                    if not self._check_grid_value(board[row][column],5): return False

                elif column <= 2 and 6 <= row <=8:
                    #print(f"Grid: 7")
                    if not self._check_grid_value(board[row][column],6): return False
                elif 3 <= column <=5 and 6 <= row <=8:
                    #print(f"Grid: 8")
                    if not self._check_grid_value(board[row][column],7): return False
                elif 6 <= column <=8 and 6 <= row <=8:
                    #print(f"Grid: 9")
                    if not self._check_grid_value(board[row][column],8): return False

        return True

if __name__ == '__main__':
    board = [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    print(Solution().isValidSudoku(board=board)) # True
    board = [["8","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    print(Solution().isValidSudoku(board=board)) # False