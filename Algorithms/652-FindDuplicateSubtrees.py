import collections

# 将树前序遍历一下，对于每个子树，都将它的根节点以及左右子树的所有节点作为key存入dict
# 这样每个不同的子树得到的key值都是唯一的（注意：中序遍历不是唯一的）
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        def pre_trav(node):
            if not node:
                return 'null'
            # key值也可以是tuple的形式，无需是str
            key = '%s,%s,%s' %(str(node.val), pre_trav(node.left), pre_trav(node.right))
            memo[key].append(node)
            return key
        
		# 其实也可以不用defaultdict，只要再建一个dict来存储子树个树即可
        memo = collections.defaultdict(list)  # 设置memo为default dict，即所有value为[]
        pre_trav(root)
        return [v[0] for k, v in memo.items() if len(v) > 1]
