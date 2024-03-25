from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def recur(pre, nums_list) -> None:
            # 返回当前排列下的所有结果
            if len(nums_list) == 1:
                res.append(pre + nums_list)
                return

            for i in range(len(nums_list)):
                recur_list = nums_list[:i] + nums_list[i+1:]
                print(recur_list)

                recur(pre + [nums_list[i]], recur_list)

        recur([], nums)

        return res


a = Solution()
num = [1, 2, 3]
print(a.permute(num))
