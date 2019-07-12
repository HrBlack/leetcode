# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    # 注意！不能直接用rand7 * rand7，这样得到的二维矩阵是对称的
    # rand7只是行、列的坐标表示
    # 临界选取40是因为可以减少运行次数，也可以选10，就是会慢很多
    def rand10(self):
        threshold = 40
        random_num = threshold + 1
        while random_num > threshold:
            random_num = 7 * (rand7() - 1) + rand7()
        return random_num % 10 + 1
