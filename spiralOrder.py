from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]: return []
        m, n = len(matrix), len(matrix[0])
        directions = [(0, 1), (1, 0),  (0, -1), (-1, 0), ] # right, down, left, up
        direction = 0
        i, j = 0, 0
        visited = set()
        spiral = []

        for _ in range(m*n):
            visited.add((i, j))
            spiral.append(matrix[i][j])
            next_i, next_j = i + directions[direction][0], j+directions[direction][1]
            
            if not (0 <= next_i < m and 0 <= next_j < n and (next_i, next_j) not in visited):
                direction = (direction+1) % 4
                next_i, next_j = i + directions[direction][0], j+directions[direction][1]

            i, j = next_i, next_j
        return spiral

if __name__ == '__main__':
    print(Solution().spiralOrder(matrix=[[]])) # []
    print(Solution().spiralOrder(matrix=[[1]])) # [1]
    print(Solution().spiralOrder(matrix=[[1, 2]])) # [1]
    print(Solution().spiralOrder(matrix=[[1], [2]])) # [1]
    print(Solution().spiralOrder(matrix=[[1,2,3],[4,5,6],[7,8,9]])) # [1,2,3,6,9,8,7,4,5]
    print(Solution().spiralOrder(matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12]])) # [1,2,3,4,8,12,11,10,9,5,6,7]
    print(Solution().spiralOrder(matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])) # [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]