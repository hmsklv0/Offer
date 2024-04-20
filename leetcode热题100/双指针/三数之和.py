# https://leetcode.cn/problems/3sum/solutions/39722/pai-xu-shuang-zhi-zhen-zhu-xing-jie-shi-python3-by/?envType=study-plan-v2&envId=top-100-liked
# 15 三数之和

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # 利用set特性去除重复
        result = set()

        # 1 数组排序
        nums.sort()

        # 2 循环查找
        nums_len = len(nums)
        for i in range(nums_len):
            if nums[i] > 0:
                break
            if i > 0 and nums[i - 1] == nums[i]:
                # 去重
                continue
            left_pointer, right_pointer = i + 1, nums_len - 1
            while left_pointer < right_pointer:
                if nums[left_pointer] + nums[right_pointer] + nums[i] == 0:
                    # 添加
                    item = tuple([nums[i], nums[left_pointer], nums[right_pointer]])
                    result.add(item)
                    left_pointer += 1
                    right_pointer -= 1

                elif nums[left_pointer] + nums[right_pointer] + nums[i] < 0:
                    left_pointer += 1
                else:
                    right_pointer -= 1

        return [list(i) for i in result]


nums = [-1, 0, 1, 2, -1, -4]
a = Solution()
print(a.threeSum(nums))
