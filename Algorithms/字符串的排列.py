# 全排列方法：同031问题
# 排列过程中直接排好了序
# 两个指针，left从右向左，找到s[left-1]>s[left]的情况；right从左向右，找到大于s[left-1]的最右位置
class Solution:
    def Permutation(self, s):
        if not s:
            return []
        s = sorted(s)  # 对字符串排序得到list，不能用s.sort()
        result = [''.join(s)]
        while True:
            left = len(s) - 1  # 每次都要重新从最后面开始遍历
            while left >= 1 and s[left-1] >= s[left]:
                left -= 1
            if left == 0:
                break
            right = left
            while right < len(s) and s[right] > s[left-1]:
                right += 1
            s[left-1], s[right-1] = s[right-1], s[left-1]
			# 将left后面的序列做逆序，因为这部分是倒序的(4, 3, 2, 1)
            right = len(s) - 1
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            result.append(''.join(s))
        return result
