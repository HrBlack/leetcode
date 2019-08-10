# DFS：iterative
# 注意这和遍历树的过程不一样，此处的DFS体现在先左后右上
class Solution:
    def hasPathSum(self, root: TreeNode, target: int) -> bool:
        if not root:
            return False
        stack = [(root, root.val)]
        while stack:
            root, value = stack.pop()
            if not root.left and not root.right:  # 确保是leaf node
                if value == target:
                    return True
            if root.left:
                stack.append((root.left, value+root.left.val))
            if root.right:
                stack.append((root.right, value+root.right.val))
        return False
