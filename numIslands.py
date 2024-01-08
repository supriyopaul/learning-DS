from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(-1, 0), (0, -1), (0, 1), (1, 0)] # up, left, right, down
        visited = set()
        count_islands = 0
        rows, columns = len(grid), len(grid[0])

        def dfs(r, c):
            if (r in [-1, rows]) or (c in [-1, columns]) or (grid[r][c] == "0") or ((r,c) in visited):
                return
            visited.add((r,c))
            dfs(r, c-1)
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c+1)
        
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == "1" and (r,c) not in visited:
                    count_islands += 1
                    dfs(r, c)
                    
        print(visited)
        return count_islands


if __name__ == "__main__":
    grid = [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
            ]
    print(Solution().numIslands(grid=grid)) # 1
    grid = [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
            ]
    print(Solution().numIslands(grid=grid)) # 3