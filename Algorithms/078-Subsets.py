# 这是一道回溯问题，同类型的还有N皇后，Combination等
# 方法一：递归版本DFS
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 思路：和人在找子集的思想一致
        # 比如先找到以1为出发点的所有子集，再去找2...
        def dfs(subset, index, result):
            # 一定要把结果先放进result里
            result.append(subset)
            for i in range(index, len(nums)):
                # 注意：如果在外面修改subset，比如append + pop会按位修改它，这样result会有影响
                dfs(subset+[nums[i]], i+1, result)
            
        result = []
        dfs([], 0, result)
        return result

# 方法二：iterative-DFS
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for i in range(len(nums)):
			# 新的子集是在当前所有子集的基础上得到的
			# 这样的写法可以省略中间变量tmp
            result.extend([item + [nums[i]] for item in result])
        return result
