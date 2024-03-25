# 题解 https://leetcode.cn/problems/product-of-array-except-self/solutions/272369/chu-zi-shen-yi-wai-shu-zu-de-cheng-ji-by-leetcode-/?envType=study-plan-v2&envId=top-100-liked

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # 做到空间复杂度为O(1)
        nums_len = len(nums)
        res = [1 for i in range(nums_len + 1)]
        start, end = 0, nums_len - 1
        pre = 1
        after = 1
        # 先将前缀乘积计算出来
        for i in range(nums_len):
            pre = pre * nums[i]
            res[i + 1] = pre
        print(res)
        # 利用前缀乘积，先从后缀的after = 1 开始计算, 因为计算当前i时需要后一位i+1的after
        for i in range(1, nums_len + 1):
            res[-i] = res[-i-1] * after
            after = after * nums[-i]

        return res[1:]

    def productExceptSelf2(self, nums: list[int]) -> list[int]:
        # 时间复杂度不变，但是空间复杂度为O(n)
        # 通过构造前后缀乘积数组，快速计算 pre[i-1] * after[i+1]
        nums_len = len(nums)
        res_pre = [0 for i in range(nums_len + 1)]
        res_after = [0 for i in range(nums_len + 1)]
        res_pre[0] = 1
        res_after[-1] = 1
        start, end = 0, nums_len - 1
        pre = 1
        after = 1

        while start < nums_len:
            pre *= nums[start]
            after *= nums[end]
            res_pre[start + 1] = pre
            res_after[end] = after

            start += 1
            end -= 1
        print(res_pre)
        print(res_after)

        res = []
        for i in range(nums_len):
            # 因为前缀乘积前面多一位
            res.append(res_pre[i] * res_after[i + 1])
        return res


a = Solution()
nums = [1, 2, 3, 4]
print(a.productExceptSelf2(nums))
print(a.productExceptSelf(nums))
