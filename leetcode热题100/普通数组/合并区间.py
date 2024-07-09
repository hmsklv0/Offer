# 题解 https://leetcode.cn/problems/merge-intervals/solutions/5411/pai-xu-by-powcai/?envType=study-plan-v2&envId=top-100-liked
# 核心思想是先排序，借助辅助数组进行逐个合并
class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:

        if len(intervals) == 1:
            return intervals
        # 1 先对列表数据进行排序
        intervals.sort(key=lambda x: x[0])

        # 2 借助res列表，记录合并后的间隔
        # 将res最新间隔（即-1）与循环中的间隔进行合并判断
        # + 若合并，修改res[-1][1]，
        # + 若不合并，则添加循环的间隔(x,y)
        res = [intervals[0]]
        for x, y in intervals[1:]:
            #
            if self.check(res[-1][0], res[-1][1], x, y):
                res[-1][1] = max(y, res[-1][1])
            else:
                res.append([x, y])

        return res

    def check(self, a, b, c, d) -> bool:
        return max(abs(b - c), abs(d - a)) <= (b - a) + (d - c)

    def merge2(self, intervals: list[list[int]]) -> list[list[int]]:
        if not intervals:
            return []
        intervals.sort()
        res = [intervals[0]]
        # 直接从 第二个区间开始判断
        for x, y in intervals[1:]:
            # 即只有一种情况不合并，那就是前一个区间的最大值  小于 当前区间的最小值
            if res[-1][1] < x:
                res.append([x, y])
            else:
                res[-1][1] = max(y, res[-1][1])
        return res


intervals_l = [[1, 3], [2, 6], [8, 10], [15, 18]]
a = Solution()
print(a.merge(intervals_l))
