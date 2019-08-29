# 方法一：栈
# 注意()()的情况
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        i = result = 0
        left = -1
        while i < len(s):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                    if not stack:
                        result = max(result, i - left)
                    else:
                        result = max(result, i - stack[-1])
                else:
                    # 左边界更新的条件是字串已经中断了
                    left = i
            i += 1
        return result

# 方法二：DP
# 注意：遇见左括号时不更新dp数组，所以这里的子串都是分段记录的
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = [0] * (len(s)+1)
        for i, item in enumerate(s):
            if item == '(':
                dp[i] = 0
            else:
				# ()(())
                if i -dp[i-1] >= 1 and s[i-1] == ')' and s[i-dp[i-1]-1] == '(':
                    dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2]
				# (())
                elif i - dp[i-1] == 1 and s[i-1] == ')' and s[i-dp[i-1]-1] == '(':
                    dp[i] = dp[i-1] + 2
				# ()()
                elif i >= 1 and s[i-1] == '(':
                    dp[i] = dp[i-2] + 2
				# ()
                elif i == 1 and s[i-1] == '(':
                    dp[i] = 2
                else:
                    dp[i] = 0
        return max(dp)
