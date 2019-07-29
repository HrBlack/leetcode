# 方法一：
# 别把问题想复杂，递归直接搞起
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
		
# 方法二：
# BFS，一层一层地往下探
# 相比于上面的递归，空间复杂度减小很多，因为可以及时释放内存
# 注意：queue里面存的都是元组，这样明显方便许多！
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = [(root, 1)]
        max_depth = 1
        while queue:
            node, depth = queue.pop(0)
            max_depth = max(max_depth, depth)
            if node.left:
                queue.append((node.left, depth+1))
            if node.right:
                queue.append((node.right, depth+1))
        return max_depth

# 方法三：
# DFS
# 注意！！和上面BFS方法除了pop的位置不同外，一模一样
# 深搜的顺序是从右边开始的
# 尝试过用中序遍历等方法来做，但是很难判断树什么时候已经遍历到最底端了
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [(root, 1)]
        max_depth = 1
        while stack:
            node, depth = stack.pop()
            max_depth = max(max_depth, depth)
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
        return max_depth
