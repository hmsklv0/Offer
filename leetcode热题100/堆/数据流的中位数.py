# https://leetcode.cn/problems/find-median-from-data-stream/solutions/2361972/295-shu-ju-liu-de-zhong-wei-shu-dui-qing-gmdo/?envType=study-plan-v2&envId=top-100-liked
# 题解
# 学习最小堆如何转为最大堆

# 一句话题解：左边大顶堆，右边小顶堆
# 小的加左边，大的加右边，平衡俩堆数，新加就弹出，堆顶给对家
# 奇数取多的，偶数取除2.
from heapq import heappush, heappop


class MedianFinder:

    def __init__(self):
        # 左边为大顶堆（若为奇数，则大顶堆比小顶堆多一个元素）
        # 右边为小顶堆
        self.Maxheap = []
        self.Minheap = []

    def addNum(self, num: int) -> None:

        if len(self.Maxheap) != len(self.Minheap):
            # 如果两个堆长度不同
            # 给 Minheap 加入新元素，元素从 Maxheap 过一次
            heappush(self.Maxheap, -num)
            heappush(self.Minheap, -heappop(self.Maxheap))
        else:
            # 如果两个堆长度相同，初始化角度想
            # 给 Maxheap 加入新元素，元素从 Minheap 过一次，
            heappush(self.Minheap, num)
            heappush(self.Maxheap, -heappop(self.Minheap))

    def findMedian(self) -> float:
        if len(self.Maxheap) != len(self.Minheap):
            # 不等，返回大顶堆头节点的相反数
            return -self.Maxheap[0]
        else:
            # 相等，则返回两个堆顶点(最大堆需要转换为相反数)的和的1/2
            return (- self.Maxheap[0] + self.Minheap[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
