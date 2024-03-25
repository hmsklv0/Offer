class Solution:
    def findRepeatNumber(self, nums: list[int]) -> int:
        # 存入字典
        nums_dic = {}

        if len(nums) <= 1:
            return None

        # 将数组存入字典
        for i in nums:
            if nums_dic.setdefault(i, 0) != 0:
                return i
            nums_dic[i] += 1
            # if i in nums_dic:
            #     # nums_dic[i] += 1
            #     return i
            # else:
            #     nums_dic[i] = 1

    def findRepeatNumber2(self, nums: [int]) -> int:
        i = 0
        # 遍历所有的索引
        while i < len(nums):
            # 索引 value 一一对应，为出现重复创造条件
            if nums[i] == i:
                # 交换完毕，进入下一个索引
                i += 1
                continue

            # 判断当前 value 值是否前面重复出现过，如果重复出现过，那么 i 对应的value值 nums[i] 作为索引时  对应的 value 值: nums[nums[i]] 应该等于 nums[i]
            # i -> nums[i]
            # nums[i] -> nums[nums[i]] 相等，证明这个值重复出现了
            if nums[nums[i]] == nums[i]:
                return nums[i]

            # 如果当前值既不等于 i, 也不属于重复出现
            # 那么将当前的值 nums[i]  交换至一一对应的地方，即 nums[i] 被交换至 nums[i]索引处 nums[nums[i]]
            # i -> nums[i]
            # nums[i] -> nums[nums[i]]
            # 即 nums[i] 与 nums[nums[i]] 进行交换
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        return -1

