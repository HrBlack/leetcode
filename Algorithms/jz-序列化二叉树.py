# 前序遍历，序列化与反序列化
class Solution:
    def __init__(self):
        self.flag = -1
    def Serialize(self, root):
        if not root:
            return '#!'
        return str(root.val) + '!' + self.Serialize(root.left) + self.Serialize(root.right)
    
    def Deserialize(self, s):
        l = s.split('!')
        self.flag += 1
        root = None
        if l[self.flag] != '#':
            root = TreeNode(int(l[self.flag]))
            root.left = self.Deserialize(s)
            root.right = self.Deserialize(s)
        return root
