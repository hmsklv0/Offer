# https://leetcode.cn/problems/add-strings/solutions/12250/add-strings-shuang-zhi-zhen-fa-by-jyd/
# 题解

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n = len(num1)
        m = len(num2)
        max_len = max(n, m) + 1
        res = [0 for i in range(max_len)]

        for i in range(0, max_len - 1):
            # 从最后一位开始计算，temp 初始化为0后进行统计
            temp = 0
            if i < n:
                temp += int(num1[-i - 1])
            if i < m:
                temp += int(num2[-i - 1])
            # 计算当前 两数之和 的位置
            index = - i - 1
            temp += res[index]
            res[index] = temp % 10
            res[index - 1] = temp // 10
            # print(res[index], res[index-1])

        if res[0] == 0:
            res = res[1:]

        return "".join(map(str, res))



