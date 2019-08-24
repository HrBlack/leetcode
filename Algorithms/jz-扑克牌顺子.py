# 两个条件就可以判断其是否为顺子
# 1. 最大值与最小值的差值；2. 数组中无重复项（除0以外）
# 不需要排序，时间O（n）
class Solution:
    def IsContinuous(self, numbers):
        if not numbers:
            return False
        maximum, minimum = -1, 14
        memo = set()
        for i in range(len(numbers)):
            if numbers[i] == 0:
                memo.add(-i)
                continue
            if numbers[i] > maximum:
                maximum = max(maximum, numbers[i])
            if numbers[i] < minimum:
                minimum = min(minimum, numbers[i])
            memo.add(numbers[i])
        if maximum - minimum > 4 or len(memo) != len(numbers):
            return False
        return True
