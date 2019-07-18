class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # dp
	# 去找以matrix[row][col]为右下角的正方形，这样它只取决于up、left和diagonal
	# 另外：本答案做到了只用一个数组来维护，注意有一个left与diag的互换
	size = 0
        if not matrix:
            return size
        prev_row = [0 for i in range(len(matrix[0]))]
        for row in range(len( matrix)):
            left = 0
            for col in range(len(matrix[0])):
                up = prev_row[col] if row > 0 else 0
                diag = prev_row[col-1] if col > 0 and row > 0 else 0
                tmp = prev_row[col]
                if matrix[row][col] == '1':
                    prev_row[col] = min(left, up, diag) + 1
                else:
                    prev_row[col] = 0
                size = max(size, prev_row[col])
                left = tmp
        return size*size  
