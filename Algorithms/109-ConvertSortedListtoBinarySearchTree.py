# 题目与108的区别就是：108是数组，这里是链表，所以只需要先把链表的value取出来即可
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        def helper(nums):
            if not nums:
                return None
            mid = len(nums)//2
            root = TreeNode(nums[mid])
            root.left = helper(nums[:mid])
            root.right = helper(nums[mid+1:])
            return root
        return helper(nums)
