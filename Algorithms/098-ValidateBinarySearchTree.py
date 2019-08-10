class Solution:
    def isValidBST(self, root, small=float('-inf'), large=float('inf')):
        if not root:
            return True
        if root.val >= large or root.val <= small:
            return False
        return self.isValidBST(root.right, max(small, root.val), large) and \
               self.isValidBST(root.left, small, min(large, root.val))

# 题目输入的是树，不是数组
# 需要注意函数的输入，应该增加root.val的左右两个边界，介于small和large之间
# 树结点向左移动时更新右边界，向右移动更新左边界
