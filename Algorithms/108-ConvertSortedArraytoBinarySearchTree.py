# 递归：DFS问题
# 题目要求：返回一颗高度平衡树（左右子树高度差不超过1）
# 思想还是要找root，即mid所在位置
# 时间 = 空间 = O（logn）= 递归深度
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        mid = len(nums)//2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root
