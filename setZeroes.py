from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        zero_locations = {"rows":set(), "cols":set()}

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_locations["rows"].add(i)
                    zero_locations["cols"].add(j)
        
        for i in range(m):
            for j in range(n):
                if i in zero_locations["rows"]: matrix[i][j] = 0
                if j in zero_locations["cols"]: matrix[i][j] = 0
        return matrix
    

if __name__ == '__main__':
    print(Solution().setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])) #[[0,0,0,0],[0,4,5,0],[0,3,1,0]]
    print(Solution().setZeroes([[1,1,1],[1,0,1],[1,1,1]])) #[[1,0,1],[0,0,0],[1,0,1]]