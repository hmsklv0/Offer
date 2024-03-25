import random


class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        i, j = 0, len(nums) - 1
        if j == nums[j]:
            return j + 1
        else:
            while i <= j:
                # if j == (nums[j-1] + nums[j]) / 2 or j + 1 == nums[j]:
                if i == j:
                    pass
                if j + 1 == nums[j]:
                    return j
                mid = (i + j) // 2
                if mid == nums[mid]:
                    i = mid
                else:
                    j = mid

    def missingNumber2(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            if i != nums[i]:
                return i

        return i + 1

    def missingNumber3(self, nums: list[int]) -> int:
        # 二分法查找
        i, j = 0, len(nums) - 1

        while i <= j:
            # 中间值，向下取整
            m = (i + j) // 2
            # 判断条件：
            if nums[m] == m:
                # miss值大于中间值
                i = m + 1
            else:
                # 如果miss值小于等于中间值
                j = m - 1
        return i



solution = Solution()
# list1 = [0, 1]
list1 = [0]

# list_t = [0, 1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(solution.missingNumber2(list1))


# for j in range(1000):
#     r1 = random.randint(7, 20000)
#     r2 = random.randint(1, r1 - 1)
#
#     list2 = [i for i in range(r1)]
#     list2.pop(r2)
    # print(r1, r2)
    # print(list2)
    # print(solution.missingNumber(list2))
    # print(j, "ok")