from heapq import heappop, heappush, heapify, heapreplace
import random
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]

    def findKthLargest2(self, nums: List[int], k: int) -> int:

        # heap = [nums[i] for i in range(k)]
        # # 堆化
        # heapq.heapify(heap)
        # for i in range(k, len(nums)):
        #     if nums[i] > heap[0]:
        #         heapq.heappop(heap)
        #         heapq.heappush(heap, nums[i])
        #     # if nums[i]>heap[0]:
        #     #     heapq.heappop(heap)
        #     #     heapq.heappush(heap,nums[i])
        # return heap[0]
        # 写法二
        # heap = nums[:k]
        # heapify(heap)
        # for i in range(k, len(nums)):
        #     if nums[i] > heap[0]:
        #         heapreplace(heap, nums[i])
        # return heap[0]

        # 写法三 在原本的数组上操作
        for i in range(len(nums)):
            nums[i] = -nums[i]
        heapify(nums)
        for i in range(k-1):
            heappop(nums)
        return -heappop(nums)

    def findKthLargest3(self, nums, k):
        # 快排
        def quick_select(nums, k):
            # 随机选择基准数
            pivot = random.choice(nums)
            big, equal, small = [], [], []
            # 将大于、小于、等于 pivot 的元素划分至 big, small, equal 中
            for num in nums:
                if num > pivot:
                    big.append(num)
                elif num < pivot:
                    small.append(num)
                else:
                    equal.append(num)
            if k <= len(big):
                # 第 k 大元素在 big 中，递归划分
                return quick_select(big, k)
            if len(nums) - len(small) < k:
                # 第 k 大元素在 small 中，递归划分
                return quick_select(small, k - (len(nums) - len(small)))
            # 第 k 大元素在 equal 中，直接返回 pivot
            return pivot

        return quick_select(nums, k)

    def findKthLargest4(self, nums, k):
        # 桶排序
        bucket = [0 for i in range(0, 20001)]

        for i in range(len(nums)):
            bucket[nums[i] + 10000] += 1

        for i in range(20000, -1, -1):
            k = k - bucket[i]
            if k <= 0:
                return i - 10000
        return 0

    def findKthLargest5(self, nums, k):
        def heapify_max2(heap: List[int], index: int, heapSize: int) -> None:
            left = index * 2 + 1
            while left < heapSize:
                # 1 左右两节点比较, 获取更大的叶子节点
                right = left + 1
                if right >= heapSize:
                    larger = left
                else:
                    larger = right if heap[right] > heap[left] else left
                # 2 子节点和父节点进行比较
                largest = index if heap[index] > heap[larger] else larger
                if largest == index:
                    # 没有必要进行交换
                    break
                else:
                    # 3 交换子节点和父节点的位置
                    heap[index], heap[largest] = heap[largest], heap[index]
                index = largest
                left = index * 2 + 1

        def buildMaxHeap(heap: List[int]) -> None:
            n = len(heap)
            for i in range(n // 2, -1, -1):
                # 自顶向下
                heapify_max2(heap, i, n)

        def heap_pop_max2(heap: List[int]) -> int:
            if len(heap) == 0:
                return -1
            heap[0], heap[-1] = heap[-1], heap[0]
            heapify_max2(heap, 0, len(heap) - 1)
            return heap.pop()

        buildMaxHeap(nums)

        for i in range(k):
            item = heap_pop_max2(nums)
        return item
