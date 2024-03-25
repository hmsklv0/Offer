# https://leetcode.cn/problems/generate-parentheses/solutions/597236/sui-ran-bu-shi-zui-xiu-de-dan-zhi-shao-n-0yt3/?envType=study-plan-v2&envId=top-100-liked
# 题解思路：先写全排列，再用条件筛选

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        pre = []
        post = ['(', ')']
        record = [0, 0]

        def dfs(cur_pre: List[str], cur_post: List[str], depth: int, cur_record) -> None:
            # 终止条件
            if depth == 2 * n:
                res.append(''.join(cur_pre))
                return

            # 递归条件
            if cur_record[0] < n:
                # 添加左括号
                cur_pre.append(cur_post[0])
                cur_record[0] += 1
                dfs(cur_pre, cur_post, depth + 1, cur_record)
                cur_record[0] -= 1
                cur_pre.pop()
            if cur_record[0] > cur_record[1] and cur_record[1] < n:
                # 仅当左括号数量大于右括号时 才能添加右括号
                cur_pre.append(cur_post[1])
                cur_record[1] += 1
                dfs(cur_pre, cur_post, depth + 1, cur_record)
                cur_record[1] -= 1
                cur_pre.pop()

        dfs(pre, post, 0, record)
        return res

    def generateParenthesis2(self, n: int) -> List[str]:
        # 增加在终止条件的限制条件，通过这种方式减少在终止条件做的判断
        res = []
        pre = []
        post = ['(', ')']
        record = [0, 0]

        def dfs(cur_pre: List[str], cur_post: List[str], depth: int, cur_record) -> None:
            # 终止条件
            # 仅当左括号数量大于右括号时 才能添加右括号,即右括号不能大于左括号数量
            # 并且括号中的值不能大于 n
            # print(cur_pre)
            if cur_record[0] > n or cur_record[1] > cur_record[0]:
                print(cur_pre, cur_record)

                return
            # print(cur_pre)
            if depth == 2 * n:
                res.append(''.join(cur_pre))
                return

            for i in range(len(cur_post)):
                cur_pre.append(cur_post[i])
                cur_record[i] += 1
                dfs(cur_pre, cur_post, depth + 1, cur_record)
                cur_record[i] -= 1
                cur_pre.pop()

        dfs(pre, post, 0, record)
        return res

a = Solution()
print(a.generateParenthesis2(3))