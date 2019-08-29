# 方法一：三指针
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        i = 1
        while i < len(s) - 2:
            j = i + 1
            while j < len(s) - 1 and j < i + 4:
                k = j + 1
                while k < len(s) and k < j + 4:
                    s1, s2, s3, s4 = s[:i], s[i:j], s[j:k], s[k:]
                    if self.is_valid_ip(s1) and self.is_valid_ip(s2) and self.is_valid_ip(s3) and self.is_valid_ip(s4):
                        result.append(s1 + '.' + s2 + '.' + s3 + '.' + s4)
                    k += 1
                j += 1
            i += 1
        return result
	# valid的条件有：值不能超过255；每段str长度不能大于3；如果一段str长度大于1，那么首位数字不能等于0
    def is_valid_ip(self, s):
        if s[0] == '0' and len(s) > 1 or len(s) >= 4 or int(s) > 255:
            return False
        return True

# 方法二：DFS递归
class Solution:
    def restoreIpAddresses(self, s):
        result = []

        def dfs(index, ip):
            if ip.count('.') == 4:
                if index == len(s):
                    result.append(ip[:-1])
                return
            for i in range(1, 4):
                if index + i <= len(s) and int(s[index:index + i]) <= 255 and (i == 1 or s[index] != '0'):
                    dfs(index + i, ip + s[index:index + i] + '.')
            return

        dfs(0, '')
        return result
