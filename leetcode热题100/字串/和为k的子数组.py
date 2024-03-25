# https://leetcode.cn/problems/subarray-sum-equals-k/solutions/238572/he-wei-kde-zi-shu-zu-by-leetcode-solution/?envType=study-plan-v2&envId=top-100-liked
# 和为k的子数组
class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        # 将所有的前缀和计算出来，将查找子数组问题转换为查找两前缀和之间的差值问题
        count = 0
        pre = 0
        pre_dict = {pre: 1}
        for i in range(len(nums)):
            pre += nums[i]
            if pre - k in pre_dict:
                count += pre_dict.get(pre - k)

            # 更新pre字典
            pre_dict[pre] = pre_dict.setdefault(pre, 0) + 1

        return count
