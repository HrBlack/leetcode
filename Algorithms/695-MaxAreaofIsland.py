# DFS问题：最大连通数
# 注意数字是不能在函数里按位修改的，list是可以的
class Solution:
    def maxAreaOfIsland(self, grid):
        if not grid or not grid[0]:
            return 0
        self.result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.result = max(self.result, self.dfs(grid, i, j))
        return self.result

    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
            return 0
        grid[i][j] = 0
        return 1 + self.dfs(grid, i+1, j) + self.dfs(grid, i-1, j) + self.dfs(grid, i, j+1) + self.dfs(grid, i, j-1)
