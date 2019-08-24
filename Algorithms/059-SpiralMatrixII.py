class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        i, j = 0, 0
        di, dj = 0, 1
        result = [[0 for _ in range(n)] for _ in range(n)]
        for index in range(n*n):
            result[i][j] = index + 1
            if result[(i+di)%n][(j+dj)%n]:
                di, dj = dj, -di
            i += di
            j += dj
        return result
