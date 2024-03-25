class Solution:
    def fib(self, n: int) -> int:
        f0 = 0
        f1 = 1
        if n == 0:
            # n = 1
            return f0
        elif n == 1:
            # n = 1
            return f1
        else:
            # n >= 2
            # 存储变量
            for i in range(2, n):
                f0, f1 = f1, f0 + f1
            # print(f0, f1, end=' ')
            return pow(f0 + f1, 1, 1000000007)


solution = Solution()
for j in range(0, 6):
    print(solution.fib(j))