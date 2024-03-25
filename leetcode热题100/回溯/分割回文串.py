# https://leetcode.cn/problems/palindrome-partitioning/solutions/640336/131-fen-ge-hui-wen-chuan-hui-su-sou-suo-yp2jq/?envType=study-plan-v2&envId=top-100-liked
#

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # 难点在于如何进行分割，并且分割的小块
        # 整体思路，即不断分割，将分割的小块不断添加入pre路径中
        # 如果切割后，后续步骤不满足回文条件，则回溯，将原本分割的小块pop，更换为另一种切割方式
        # 直到尝试成功，post 没有需要进行的元素了，将 pre 添加进入 res
        pre = []
        post = list(s)
        res = []

        def dfs(cur_pre: List[str], cur_post: List[str]):
            # 终止条件
            if len(cur_post) == 0:
                res.append(cur_pre[:])
                return

            # 理解如何切割，即对 post 进行切片，不需要记录切割符
            # 将切割后的片段加入 pre，类似于添加路径
            for i in range(len(cur_post)):
                tmp = cur_post[:i + 1]
                if self.isPalindrome(tmp):
                    cur_pre.append(''.join(tmp))
                    next_post = cur_post[i + 1:]
                    dfs(cur_pre, next_post)
                    cur_pre.pop()

            return

        dfs(pre, post)
        return res

    def isPalindrome(self, s: List[str]) -> bool:
        # 双指针判断回文
        start, end = 0, len(s) - 1
        while start < end:
            if s[start] != s[end]:
                return False
            else:
                start += 1
                end -= 1
        return True
