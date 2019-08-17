# 递归：DFS
# 思路：分别求以每个node为root的子树路径中的最大路径和，只需要遍历一遍树
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.maximum = float('-inf')
        def helper(root):
            if not root:
                return 0
            left = max(0, helper(root.left))
            right = max(0, helper(root.right))
            self.maximum = max(self.maximum, root.val + left + right)
            return max(left, right) + root.val
        helper(root)
        return self.maximum
