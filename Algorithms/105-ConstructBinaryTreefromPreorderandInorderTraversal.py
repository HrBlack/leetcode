# 递归：DFS问题
# 思想：找到某棵树root在preorder和inorder中的位置，则两侧分别为左右子树
class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        value = preorder[0]
        index = inorder.index(value)  # 优化就是将inorder存入字典
        root = TreeNode(value)
        root.left = self.buildTree(preorder[1:index+1], inorder[:index])
        root.right = self.buildTree(preorder[index+1:], inorder[index+1:])
        return root
