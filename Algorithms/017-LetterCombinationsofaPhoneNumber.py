# BFS方法：queue
# 注意：此题有一个i指针需要维护，在队列中无法检测i是否应该变化；
# 在这里我取巧利用了队列中的第一个元素的长度来判断i
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return ''
        memo_dict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                     '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        result = [v for v in memo_dict[digits[0]]]
        i = 1
        while result and i < len(digits):
            num = result.pop(0)
            for item in memo_dict[digits[i]]:
                result.append(num+item)
            i = len(result[0])
        return result

# BFS方法：辅助数组
# 通过维护一个level数组，来不断与result进行交换；
# 这种方法中i指针的维护较为合理，直接通过level是否为空来判断
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return ''
        memo_dict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                     '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        level = [v for v in memo_dict[digits[0]]]
        i = 1
        if len(digits) == 1:
            return level
        while i < len(digits):
            result = []
            while level:
                num = level.pop()
                for item in memo_dict[digits[i]]:
                    result.append(num + item)
            level = result
            i += 1
        return result

# BFS方法：递归
# 简单明了
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return ''
        memo_dict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                     '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        def helper(level, i):
            if i == len(digits):
                return level
            level = [item + v for item in level for v in memo_dict[digits[i]]]
            return helper(level, i+1)
        return helper([''], 0)
