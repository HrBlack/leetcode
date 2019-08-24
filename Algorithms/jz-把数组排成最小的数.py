# 思想：将numbers中的字符串进行排序，排序原则如下
# 若a + b < b + a，则a < b，a和b皆为字符串
# 注意cmp的用法
class Solution:
    def PrintMinNumber(self, numbers):
        if not numbers:
            return ''
        nums = list(map(str, numbers))
        nums.sort(cmp=lambda x, y: cmp(x+y, y+x))
        return ''.join(nums).lstrip('0')
