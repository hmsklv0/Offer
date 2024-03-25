# https://leetcode.cn/problems/letter-combinations-of-a-phone-number/solutions/839901/dai-ma-sui-xiang-lu-17-dian-hua-hao-ma-d-ya2x/?envType=study-plan-v2&envId=top-100-liked
# 题解

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num2char = {'2': ['a', 'b', 'c'],
                    '3': ['d', 'e', 'f'],
                    '4': ['g', 'h', 'i'],
                    '5': ['j', 'k', 'l'],
                    '6': ['m', 'n', 'o'],
                    '7': ['p', 'q', 'r', 's'],
                    '8': ['t', 'u', 'v'],
                    '9': ['w', 'x', 'y', 'z']
                    }
        res = []

        def dfs(cur_pre: List[str], cur_post: list[str]) -> None:
            if len(cur_post) == 0:
                res.append(''.join(cur_pre))
                return

            post_list = num2char[cur_post[0]]

            for i in range(len(post_list)):
                cur_pre.append(post_list[i])
                dfs(cur_pre, cur_post[1:])
                cur_pre.pop()

        pre, post = [], list(digits)
        dfs(pre, post)

        return res

a = Solution()
digits = "23"
print(a.letterCombinations(digits))