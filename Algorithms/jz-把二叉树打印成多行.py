# 层序遍历二叉树
# 典型BFS，之前一直是用辅助数组来存每层的节点，但那样的话空间复杂度高一些
# 这里用了queue来做，注意第二个while的用法
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, root):
        if not root:
            return []
        queue = [root]
        result = [[root.val]]
        while queue:
            start, end = 0, len(queue) - 1
            values = []
            while start <= end:  # 此处用法巧妙
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                    values.append(node.left.val)
                if node.right:
                    queue.append(node.right)
                    values.append(node.right.val)
                start += 1
            if not values:
                break
            result.append(values)
        return result
