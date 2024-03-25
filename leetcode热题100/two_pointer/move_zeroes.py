# https://leetcode.cn/problems/move-zeroes/solutions/489622/yi-dong-ling-by-leetcode-solution/?envType=study-plan-v2&envId=top-100-liked
# 283. 移动零

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 快慢指针，如果出现有零的情况，那么快指针将比慢指针更快
        # 出现一个零，领先一个
        # 出现两个零，领先两个
        # 因此推导出两个性质：
        # + 右指针左边直到左指针处均为零（即为两者相差的距离）
        # + 左指针左边均为非零数
        left_pointer = 0
        right_pointer = 0

        """
        什么时候开始？
        当出现第一个零，快指针比慢指针快了一个，然后快指针指向了非零值，而慢指针这时候指向零，
        中间和快指针之间的距离全部为0（不包含快指针指向的位置），开始零和非零值交换
        
        什么时候结束？
        可以想象中间夹着全零值的双指针到了末尾，然后如果最后一个值为0，那么快指针直接+1，等于数组长度，退出
        如果，最后一个值非零，那么快指针和慢指针的值交换后，快指针和慢指针同时+1，然后快指针等于数组长度，退出
        """
        n = len(nums)
        while right_pointer < n:
            if nums[right_pointer] != 0:
                # 因此每次交换，都是将左指针的零与右指针的非零数交换，且非零数的相对顺序并未改变。
                nums[left_pointer], nums[right_pointer] = nums[right_pointer], nums[left_pointer]
                left_pointer += 1
            right_pointer += 1



    def moveZeroes2(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        zeroes_list = []
        for i in range(len(nums)):
            if nums[i] == 0:
                zeroes_list.append(i)

        move_step = 0
        for i in range(len(nums)):
            if i - 1 in zeroes_list:
                # 将前进的 step 找出
                move_step = zeroes_list.index(i - 1) + 1
            nums[i - move_step] = nums[i]

        for i in range(len(nums) - len(zeroes_list),  len(nums)):
            nums[i] = 0

a = Solution()
a_list = [1]
a.moveZeroes(a_list)
print(a_list)