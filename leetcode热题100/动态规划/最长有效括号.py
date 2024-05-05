from typing import List


# https://leetcode.cn/problems/longest-valid-parentheses/solutions/314683/zui-chang-you-xiao-gua-hao-by-leetcode-solution/?envType=study-plan-v2&envId=top-100-liked
# 题解

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # 自己的思路
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

    def longestValidParentheses3(self, s: str) -> int:
        # 使用栈解决,栈存储索引
        # ( 栈增加
        # 遇到) 栈pop
        # 用 当前索引减去栈顶元素的索引,就可以得到连续的有效括号的长度,也是当前 ) 结尾的数组的最长连续有效括号长度
        # 为了保证一直有栈顶元素, 在栈顶加入 -1 元素代表一个 最后一个没有被匹配的右括号的下标
        # 测试数据 ()()()
        # 第二个 ) 栈 )(  计算: 1 - (-1) = 2
        # 第四个 ) 栈 )(  计算: 3 - (-1) = 4
        # 第六个 ) 栈 )(  计算: 5 - (-1) = 6
        # 同样地 例子 )()()()
        # 取代了了 之前的 索引为 -1 的右括号, 改为 索引为 0 的右括号
        # 2 - 0
        # 4 - 0
        # 6- 0

        stack = [-1]
        res = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    # 中间pop出的括号为连续的最长有效括号
                    res = max(res, i - stack[-1])
        return res


ss = ")()())"
a = Solution()
print(a.longestValidParentheses(ss))
