class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        if not matrix:
            return
		# dp[0][:]与dp[:][0]是为了单行单列的matrix准备的
        self.dp = [[0 for i in range(len(matrix[0])+1)] for j in range(len(matrix)+1)]
        for i in range(1, len(matrix)+1):
            for j in range(1, len(matrix[0])+1):
                # dp[i][j]中记录的是以matrix[i-1][j-1]为右下角元素的子矩阵和
                self.dp[i][j] = self.dp[i-1][j] + self.dp[i][j-1] - self.dp[i-1][j-1] + matrix[i-1][j-1]
                
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.dp[row2+1][col2+1] - self.dp[row1][col2+1] - self.dp[row2+1][col1] + self.dp[row1][col1]
