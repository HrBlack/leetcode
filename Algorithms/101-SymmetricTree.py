# 递归方法：
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def helper(left, right):
            if not left and not right:
                return True
            if left and right and left.val == right.val:
                return helper(left.right, right.left) and helper(right.right, left.left)
            return False
        
        if root:
            return helper(root.left, root.right)
        return True
