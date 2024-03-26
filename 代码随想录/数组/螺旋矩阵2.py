# https://programmercarl.com/0059.%E8%9E%BA%E6%97%8B%E7%9F%A9%E9%98%B5II.html#%E7%AE%97%E6%B3%95%E5%85%AC%E5%BC%80%E8%AF%BE

from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        layer = n // 2
        index = 0
        res = [[0 for _ in range(n)] for _ in range(n)]
        a, b = 0, n - 1
        c, d = 0, n - 1
        count = 0
        while index <= layer:

            # 左 -> 右
            row = c
            for i in range(a, b + 1):
                count += 1
                res[row][i] = count
            # 上 -> 下
            column = b
            for j in range(c + 1, d + 1):
                count += 1
                res[j][column] = count
            # 右 -> 左
            row = d
            for i in range(b - 1, a - 1, -1):
                count += 1
                res[row][i] = count
            # 下 -> 上
            column = a
            for j in range(d - 1, c, -1):
                count += 1
                res[j][column] = count
            a += 1
            b -= 1
            c += 1
            d -= 1
            index += 1
        return res
