class Solution:
    def exchange(self, nums: list[int]) -> list[int]:
        list_len = len(nums)
        i, index = 0, 0
        while i < list_len:
            i += 1
            if nums[index] % 2 == 0:
                cur = nums.pop(index)
                nums.append(cur)
            else:
                index += 1

        return nums

    def exchange2(self, nums: list[int]) -> list[int]:
        i, j = 0, len(nums) - 1

        while i < j:
            while i < j and nums[i] & 1 == 1:
                # 从左往右 找到偶数
                i += 1
            while i < j and nums[j] & 1 == 0:
                # 从右往左 找到奇数
                j -= 1
            # 临界条件 i == j，两者皆为偶数
            nums[i], nums[j] = nums[j], nums[i]

        return nums


list1 = [1, 2, 3, 4]
solution = Solution()
print(solution.exchange(list1))
