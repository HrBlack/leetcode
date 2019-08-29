# 第一行作为列指针，第一列作为行指针，如果i行j列的值为0，则将该行列下的两个指针置为0
# 注意：(0, 0)点在这里被看作行指针，所以又维持了一个单独的列指针is_col来检测第一列
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        R = len(matrix)
        C = len(matrix[0])
        is_col = False
        for row in range(R):
            if matrix[row][0] == 0:
                is_col = True
            for col in range(1, C):
                if matrix[row][col] == 0:
                    matrix[row][0] = matrix[0][col] = 0
        for r in range(1, R):
            for c in range(1, C):
                if not matrix[0][c] or not matrix[r][0]:
                    matrix[r][c] = 0
        if matrix[0][0] == 0:
            for j in range(1, C):
                matrix[0][j] = 0
        if is_col:
            for i in range(R):
                matrix[i][0] = 0
