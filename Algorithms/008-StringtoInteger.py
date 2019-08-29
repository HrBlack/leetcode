class Solution:
    def myAtoi(self, str: str) -> int:
        i, sign = 0, 1
        result = []
        str = str.strip()
        if not str:
            return 0
        if str[0] in ['-', '+']:
            if str[0] == '-':
                sign = -1
            i = 1
        while i < len(str) and str[i].isdigit():
            result.append(str[i])
            i += 1
        if not result:
            return 0
        return max(min(sign * int(''.join(result)), 2 ** 31 - 1), -2 ** 31)
