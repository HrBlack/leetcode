# 回溯法：
# 每个点的search方向都有4个，避免重复采用memo矩阵
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        memo = [[0 for i in range(cols)] for j in range(rows)]
        def helper(r, c, path):
            if not path:
                return True
            if rows > r >= 0 and cols > c >= 0 and memo[r][c]!=1 and matrix[r*cols+c] == path[0]:
                memo[r][c] = 1
                if helper(r+1, c, path[1:]) or helper(r-1, c, path[1:]) or helper(r, c-1, path[1:])or helper(r, c+1, path[1:]):
                    return True
                memo[r][c] = 0  # 说明[r, c]匹配到了path中元素，但是后续没有成功匹配
                return False
            else:
                return False

        for i in range(rows):
            for j in range(cols):
                if helper(i, j, path):
                    return True
        return False
