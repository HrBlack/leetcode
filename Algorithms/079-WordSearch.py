# DFS问题：
# 和jz中的矩阵路径一题思路一致
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        memo = [[0 for i in range(len(board[0]))] for j in range(len(board))]
        def dfs(row, col, word):
            result = False
            if not word:
                return True
            if 0 <= row < len(board) and 0 <= col < len(board[0]) and memo[row][col] != 1 and board[row][col] == word[0]:
                memo[row][col] = 1
                result = dfs(row+1, col, word[1:]) or dfs(row, col+1, word[1:]) or dfs(row, col-1, word[1:]) or dfs(row-1, col, word[1:])
                memo[row][col] = 0
            return result
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and dfs(i, j, word):
                    return True
        return False
