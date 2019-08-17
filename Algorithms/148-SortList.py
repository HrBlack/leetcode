# 链表排序：题目要求时间nlogn，空间O(1)
# 方法一：归并
# 归并正常是O（n）的空间复杂度，因为递归每层都要有辅助数组，这里利用链表指针交换，实现按位修改
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
	    # sortList函数是对某个链表排序，merge函数是对两个链表做归并
        if not head or not head.next:  # 链表长度<=1时
            return head
		# 二分链表，一段是以head为首，一段以slow为首
        prev, slow, fast = None, head, head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None  # 把原链表断开
        head1 = self.sortList(head)
        head2 = self.sortList(slow)
        return self.merge(head1, head2)

    def merge(self, head1, head2):
        if not head1 or not head2:  # 二选一时这样写很高效
            return head1 or head2
        if head1.val > head2.val:  # 把val小的链表给head1
            head1, head2 = head2, head1
        head = prev = head1
        head1 = head1.next
        while head1 and head2:
            if head1.val < head2.val:
                prev.next = head1
                head1 = head1.next
            else:
                prev.next = head2
                head2 = head2.next
            prev = prev.next
		# head1与head2至少有一个为None
        prev.next = head1 or head2
        return head

# 方法二：快排，值交换，按位修改
# p，q两个指针，使p前面的node都是小于pivot的，p和q之间的node都是大于pivot的
# 时间O（nlogn）；空间O（logn）；在lc中无法通过
class Solution:
    def sortList(self, head, end=None) -> ListNode:
        def quick_sort(front, end):
            pivot = front.val 
            p, q = front, front.next
            while q != end:
                if q.val < pivot:
                    p = p.next
                    p.val, q.val = q.val, p.val
                q = q.next
            p.val, front.val = front.val, p.val
            return p
        if head != end:
            partition = quick_sort(head, end)
            self.sortList(head, partition)
            self.sortList(partition.next, end)
        return head
