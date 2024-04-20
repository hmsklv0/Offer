# 128. 最长连续序列
# https://leetcode.cn/problems/longest-consecutive-sequence/?envType=study-plan-v2&envId=top-100-liked
# 题解 https://leetcode.cn/problems/longest-consecutive-sequence/solutions/2362995/javapython3cha-xi-biao-ding-wei-mei-ge-l-xk4c/?envType=study-plan-v2&envId=top-100-liked
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # 将数组转为字典
        nums_dict = {}
        for i in nums:
            nums_dict[i] = i
        nums_dict = set()

        # 查找起点
        start = []
        for i in nums:
            if i - 1 not in nums_dict:
                start.append([i])

        # 起点查询长度
        for i in range(len(start)):
            start_num = start[i][0]
            temp_num = start_num
            while 1:
                temp_num = temp_num + 1
                if temp_num in nums_dict:
                    start[i].append(temp_num)
                else:
                    break
        # 最长连续
        longest_num = 0
        for i in range(len(start)):
            longest_num = max(longest_num, len(start[i]))

        return longest_num

    def longestConsecutive2(self, nums: list[int]) -> int:
        # 优化1 将数组转为集合，去除冗余元素
        nums_set = set(nums)

        # 优化2 优化根据起点判断连续数组长度
        # 查找起点
        longest_num = 0
        # 优化3 优化查询对象，只查询集合中的元素，避免重复查询
        for i in nums_set:
            if i - 1 not in nums_set:
                # 找到起点
                temp_num = i
                seq_len = 1

                while temp_num + 1 in nums_set:
                    temp_num += 1
                    seq_len += 1

                longest_num = max(longest_num, seq_len)

        return longest_num


a = Solution()
print(a.longestConsecutive2([100, 4, 200, 1, 3, 2]))
