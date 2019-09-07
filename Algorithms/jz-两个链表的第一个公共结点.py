# 此解法不需要提前遍历一次链表以获得长度差值
# 假设我们有p1:0-1-2-3-4-5-null和p2:a-b-4-5-null，算法相当于将两者拼接起来
# 0-1-2-3-4-5-null(此时遇到ifelse)-a-b-4-5-null
# a-b-4-5-null(此时遇到ifelse)0-1-2-3-4-5-null
# 这样在4-5-null的地方就找到了相同的位置
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        p1, p2 = pHead1, pHead2
        while p1 != p2:
            p1 = p1.next if p1 else pHead2
            p2 = p2.next if p2 else pHead1
        return p1
