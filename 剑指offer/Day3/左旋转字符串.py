class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:] + s[:n] if n < len(s) else None

str_t = '1234567'
solution = Solution()
print(solution.reverseLeftWords(str_t, 2))