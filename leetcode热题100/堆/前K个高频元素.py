import collections
from typing import List
import heapq

# https://leetcode.cn/problems/top-k-frequent-elements/solutions/611626/347-qian-k-ge-gao-pin-yuan-su-zhi-jie-pa-wemd/?envType=study-plan-v2&envId=top-100-liked
# 堆排序思路
# 序列比较大小（包括元组）https://docs.python.org/3/tutorial/datastructures.html

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 直接调用 collections.Counter API实现
        nums_dict = collections.Counter(nums)

        res = [key for key, _ in nums_dict.most_common()[:k]]
        return res

    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}
        for i in range(len(nums)):
            if nums[i] in nums_dict:
                nums_dict[nums[i]] += 1
            else:
                nums_dict[nums[i]] = 1
        nums_count = [(k, v) for k, v in nums_dict.items()]
        nums_count.sort(key=lambda s: s[1], reverse=True)
        del nums_dict
        return [key for key, _ in nums_count[:k]]

    def topKFrequent3(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}
        for i in range(len(nums)):
            if nums[i] in nums_dict:
                nums_dict[nums[i]] += 1
            else:
                nums_dict[nums[i]] = 1
        nums_count = [(k_, v_) for k_, v_ in nums_dict.items()]
        res = heapq.nlargest(k, nums_count, key=lambda item: item[1])
        return [key for key, _ in res]

    def topKFrequent4(self, nums: List[int], k: int) -> List[int]:
        # 使用最小堆实现存储最大的k个元素，只要比堆顶元素大，就入堆
        # 借助堆实现
        nums_dict = collections.Counter(nums)

        heap = []
        for key, value in nums_dict.items():
            if len(heap) >= k:
                if value > heap[0][0]:
                    # 如果大于最小堆的堆顶，才进行堆顶交换操作
                    heapq.heapreplace(heap, (value, key))
            else:
                # 元组可以比较，这就是添加 (value, key) 的原因，由于元组比较的时候优先从第一个元素开始比较大小
                heapq.heappush(heap, (value, key))

        return [item[1] for item in heap]
