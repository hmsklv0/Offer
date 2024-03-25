from typing import List


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        s_len = len(s)
        # 记录当前连续字串长度
        dp = [0 for _ in range(s_len + 1)]
        # 辅助数组记录状态，表示当前dp是否可以接续
        dp_st = [False for _ in range(s_len + 1)]
        dp_st[0] = True
        # 配合栈，计算
        stack: List[tuple[str, int]] = []
        result = 0
        if len(s) <= 1:
            return 0

        for i in range(1, s_len + 1):
            ch = s[i - 1]
            if ch == ')' and len(stack) != 0:
                cur_ch, cur_index = stack.pop()
                if dp_st[cur_index] == True:
                    # 续接上最前面的那一段
                    dp[i] = dp[cur_index] + i - cur_index
                else:
                    # 不能续接，就将stack记录的这一段进行赋值
                    dp[i] = i - cur_index
                dp_st[i] = True
            elif ch == '(':
                stack.append((ch, i - 1))

            result = max(result, dp[i])
        print(dp)
        return result

    def longestValidParentheses2(self, s: str) -> int:
        # 相较于方法1，仅仅优化部分代码，
        s_len = len(s)
        # 记录当前连续字串长度
        dp = [[0, False] for _ in range(s_len + 1)]

        # 配合栈，计算
        stack: List[int] = []
        result = 0
        if len(s) <= 1:
            return 0

        for i in range(1, s_len + 1):
            if s[i - 1] == ')' and len(stack) != 0:
                cur_index = stack.pop()
                if dp[cur_index][1] == True:
                    # 续接上最前面的那一段
                    dp[i][0] = dp[cur_index][0] + i - cur_index
                else:
                    # 不能续接，就将stack记录的这一段进行赋值
                    dp[i][0] = i - cur_index
                dp[i][1] = True
            elif s[i - 1] == '(':
                stack.append(i - 1)

            result = max(result, dp[i][0])

        return result


ss= ")()())"
a = Solution()
print(a.longestValidParentheses(ss))
