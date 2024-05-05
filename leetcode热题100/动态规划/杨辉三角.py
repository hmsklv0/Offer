# https://leetcode.cn/problems/pascals-triangle/solutions/510638/yang-hui-san-jiao-by-leetcode-solution-lew9/?envType=study-plan-v2&envId=top-100-liked
# 官方题解：更加优雅
# https://leetcode.cn/problems/pascals-triangle/solutions/53504/qu-qiao-jie-fa-cuo-yi-wei-zai-zhu-ge-xiang-jia-28m/?envType=study-plan-v2&envId=top-100-liked
# 题解 取巧解法：错一位再逐个相加
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]

        res.append([1])
        res.append([1, 1])

        numRow_list = [1, 1]
        for i in range(3, numRows + 1):
            new_numRow_list = [1]

            for j in range(len(numRow_list) - 1):
                num = numRow_list[j] + numRow_list[j + 1]
                new_numRow_list.append(num)
            new_numRow_list.append(1)
            res.append(new_numRow_list)
            numRow_list = new_numRow_list

        return res

    def generate2(self, numRows: int) -> List[List[int]]:
        # 上一层的错位相加，补零
        # 0 1 2 1
        # 1 2 1 0
        if numRows == 0:
            return []
        res = [[1]]
        while len(res) < numRows:
            newRow = [a + b for a, b in zip([0] + res[-1], res[-1] + [0])]
            res.append(newRow)
        return res


c = Solution()

for i in range(1, 6):
    print(i, '\n', c.generate(i))
