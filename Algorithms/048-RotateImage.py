# 顺时针旋转：先沿垂直方向取reverse，再做转秩
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix[:] = map(list, zip(*matrix[::-1]))

# 逆时针旋转：左右方向取reverse，再做转秩
