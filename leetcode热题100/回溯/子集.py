# https://leetcode.cn/problems/subsets/solutions/850474/dai-ma-sui-xiang-lu-78-zi-ji-hui-su-sou-6yfk6/?envType=study-plan-v2&envId=top-100-liked

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[], nums]

        res = []
        res_set = set()

        def dfs(pre: List[int], post: List[int]) -> None:
            pre.sort()
            pre_str = str(pre)
            # print(pre_str, pre)

            if pre_str not in res_set:
                res.append(pre)
                res_set.add(pre_str)
            for i in range(len(post)):
                copy_pre = pre[:]
                copy_pre.append(post[i])
                copy_post = post[:]
                copy_post.remove(post[i])
                dfs(copy_pre, copy_post)

        dfs([], nums)
        return res

    def subsets2(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(cur_pre: List[int], cur_post: List[int]) -> None:
            res.append(cur_pre[:])
            if len(cur_post) == 0:
                return

            for j in range(len(cur_post)):
                # 下一次迭代对象
                next_pre = cur_pre[:]
                next_pre.append(cur_post[j])
                next_post = cur_post[j+1:]
                print(next_pre, next_post)
                # 迭代
                dfs(next_pre, next_post)

        dfs([], nums)
        return res


a = Solution()
num = [1, 2, 3]

print(a.subsets2(num))
