# DFS最大连通问题
# 题目说了只有一个连通块，所以每个1都可以+4的边长；如果左边和上边已经有了1，那么就-2
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    result += 4
                    if i > 0 and grid[i-1][j] == 1:
                        result -= 2
                    if j > 0 and grid[i][j-1] == 1:
                        result -= 2
        return result
