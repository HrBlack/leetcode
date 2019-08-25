# 思想：先利用fast找到tail和length，然后交换即可，所以要遍历链表两次
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        slow = fast = head
        length = 0
        while fast:
            tail = fast
            fast = fast.next
            length += 1
        if length == 0:
            return head
        for i in range(length-k%length-1):
            slow = slow.next
        tail.next = head
        head = slow.next
        slow.next = None
        return head
