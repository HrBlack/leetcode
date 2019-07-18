# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 时间复杂度为O(max(l1, l2))
        # 注意要想给root.next赋值就要先建ListNode的类
        result = ListNode(0)
        root = result
        addition = 0
        while l1 or l2:
            addition //= 10  # 记录carry进位
            if l1:
                addition += l1.val
                l1 = l1.next
            if l2:
                addition += l2.val
                l2 = l2.next
            root.next = ListNode(addition % 10)
            root = root.next
        if addition >= 10:
            root.next = ListNode(addition // 10)
        return result.next
