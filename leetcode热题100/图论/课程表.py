# https://mp.weixin.qq.com/s/RecRcPHQTLnxZTw4j4Hn5A
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # 使用拓扑排序的思想解决，
        # 拓扑排序是一种对有向无环图（DAG）进行排序的算法。
        # 在拓扑排序中，对于每个有向边 (u, v)，顶点 u 在排序中必须出现在顶点 v 的前面。
        # 换句话说，拓扑排序将 DAG 中的所有顶点排成一个线性序列，
        # 使得对于所有的有向边 (u, v)，顶点 u 在顶点 v 的前面。

        # 1 记录有向边、顶点入度
        ingree = [0 for i in range(numCourses)]
        preCourse = [[] for i in range(numCourses)]
        for i in range(len(prerequisites)):
            preCourse[prerequisites[i][0]].append(prerequisites[i][1])
            ingree[prerequisites[i][1]] += 1

        # 2 所有入度为0的课程入队列
        queue = []
        count = 0
        for course in range(len(ingree)):
            if ingree[course] == 0:
                queue.append(course)
                count += 1

        # 3 利用循环，
        # 当队列不为空，从队列中取出一个元素将此元素对应的所有先修课程的入度减1，
        # 并将入度为0的先修课程存入队列用count计数
        while queue:
            cur_course = queue.pop()

            for i in range(len(preCourse[cur_course])):
                # 入度 - 1
                ingree[preCourse[cur_course][i]] -= 1
                if ingree[preCourse[cur_course][i]] == 0:
                    queue.append(preCourse[cur_course][i])
                    count += 1

        if count == numCourses:
            return True
        else:
            return False
