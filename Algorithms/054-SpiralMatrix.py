# 打印旋转矩阵
# 这个实现方法特别好，把边界条件都统一到了一个表达式里
class Solution:
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        result = []
        i, j = 0, 0
        di, dj = 0, 1  # i和j的移动步伐
        for index in range(len(matrix * len(matrix[0]))):
            result.append(matrix[i][j])
            matrix[i][j] = None
			# 现在已经走到头了，再走一步就是None
            if matrix[(i+di) % len(matrix)][(j+dj) % len(matrix[0])] is None:
                di, dj = dj, -di
            i += di
            j += dj
        return result
