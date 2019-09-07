# DFS解法：
# 给定一个初始点，四周寻找，直到所有的连通项被置为0
# 时间：O（row*col）
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:            
        if not grid or not grid[0]:
            return 0
        row, col = len(grid), len(grid[0])
        count = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1':
                    self.dfs(grid, r, c)
                    count += 1
        return count

    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '0'
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)
