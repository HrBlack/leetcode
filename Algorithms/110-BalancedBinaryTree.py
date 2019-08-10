# 递归：DFS问题
# 时间 = 空间 = O(n)，虽然递归深度是nlogn，但是每层中的每个点都要遍历
class Solution:
    def isBalanced(self, root):
        # get height函数不光得到子树高度，还会判断它是不是平衡树
        def get_height(root):
            if not root:
                return 0
            left = get_height(root.left)
            right = get_height(root.right)
            if abs(left-right) > 1:
                self.flag = False
            return 1 + max(left, right)
        
        if not root:
            return True
        self.flag = True
        get_height(root)  # 按位修改全局变量self.flag
        return self.flag
