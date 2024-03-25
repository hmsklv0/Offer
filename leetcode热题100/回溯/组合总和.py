from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 思路与子集类似
        # 以2，3，5举例
        # 子树遍历，每次遍历的post以当前节点开始，抛弃之前的部分，即 post[i:]
        # 2
        # 2             3       5
        # 2     3   5   3 5     5
        # 2 3 5 3 5 5
        res = []

        def dfs(pre: List[int], post: List[int], target: int):
            sum_pre = sum(pre)
            if sum_pre == target:
                # 直接使用pre会导致对象错误
                res.append(pre[:])
                return
            elif sum_pre > target:
                return

            for i in range(len(post)):
                pre.append(post[i])
                next_post = post[i:]
                dfs(pre, next_post, target)
                pre.pop()

        dfs([], candidates, target)
        return res
