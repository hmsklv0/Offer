# https://leetcode.cn/problems/3sum/solutions/39722/pai-xu-shuang-zhi-zhen-zhu-xing-jie-shi-python3-by/?envType=study-plan-v2&envId=top-100-liked
# 15 三数之和

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # 利用set特性去除重复
        result = set()

        # 1 数组排序
        nums.sort()

        # 2 循环查找
        for i in range(len(nums)):

            if nums[i] > 0:
                # 排序之后如果第一个元素已经大于零，那么无论如何组合都不可能凑成三元组，直接返回结果就可以了
                break

            if i >= 1 and nums[i] == nums[i - 1]:
                # 去重
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    item = tuple([nums[i], nums[left], nums[right]])
                    result.add(item)
                    left += 1
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1
        return [list(i) for i in result]
