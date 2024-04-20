# https://leetcode.cn/problems/multiply-strings/solutions/7629/python-zi-fu-chuan-bao-li-mo-ni-shu-shi-cheng-fa-j/
# 题解
class Solution:
   def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        m = len(num1)
        n = len(num2)
        res = [0 for _ in range(m + n)]
        for i in range(0, m):
            for j in range(0, n):
                temp = int(num1[-i - 1]) * int(num2[-j - 1])
                index = -(i + j + 1)
                print(temp)

                temp += res[index]
                res[index] = temp % 10
                # 加上进位，而不是等于进位
                res[index - 1] += temp // 10
                print("".join(map(str, res)))

        if res[0] == 0:
            res = res[1:]
        return "".join(map(str, res))


a = Solution()
num1 = "123"
num2 = "456"
print(a.multiply(num1, num2))
