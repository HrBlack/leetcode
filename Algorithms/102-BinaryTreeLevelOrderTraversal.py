# BFS
# 注意：题目要求的输出形式是每一层单独放进一个list中，所以没办法用queue来做
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res, level = [], [root]
        # 注意：level里存的一定是node，而不是value
        while level:
            temp = []
            res.append([node.val for node in level])
            for item in level:
                if item.left:
                    temp.append(item.left)
                if item.right:
                    temp.append(item.right)
            level = temp
        return res
