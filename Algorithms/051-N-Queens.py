# DFS
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        def dfs(queen, add, diff):
            if len(queen) == n:
                res.append(queen)
                return
            for row in range(n):
                col = len(queen) - 1
                if row not in queen and col + row not in add and col - row not in diff:
                    dfs(queen + [row], add + [col+row], diff + [col-row])
            return

        dfs([], [], [])
        return [['.' * i + 'Q' + '.' * (n-i-1) for i in queen] for queen in res]
                    
