class Solution:
    def numWays(self, n: int) -> int:
        count = 0
        def findway(rest):
            nonlocal count
            if rest == 0:
                count += 1
                return
            elif rest < 0:
                return
            findway(rest - 1)
            findway(rest - 2)
        findway(n)
        return count % 1000000007

    def numWays2(self, n: int) -> int:
        a, b = 1, 1
        for _ in range(n):
            a, b = b, a + b
        return a % 1000000007


solution = Solution()
print(solution.numWays2(36))

