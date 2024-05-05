# https://blog.csdn.net/dream_follower/article/details/105202811
# 图解大根堆的堆排序

# https://zhuanlan.zhihu.com/p/266665145
# 为什么堆化 heapify() 只用 O(n) 就做到了？
# 理论证明堆化的比较次数的复杂度为 O(n)

# https://baijiahao.baidu.com/s?id=1753904109422547868&wfr=spider&for=pc
# 深刻理解堆和堆排序以及在 Python 中的应用

# 堆的操作
# 1 实现堆，借助heapify对现有列表就地转化为堆O(n)、或者借助heap_push实现堆O(nlogn)
# 2 堆的pop
# + 最大堆实现: 交换首尾，heapify，弹出堆列表的尾

# 3 堆的push 自顶向下
#


from typing import List
import heapq
# 大根堆
max_heap = []


def heapInsert(heap: List[int], index: int) -> None:
    # while 循环的终止条件是当前节点比它的父节点小，当index为0的时候，(index-1)/2也为0，循环也会终止。
    if index <= 0:
        return
    while heap[index] > heap[(index - 1) // 2]:
        heap[index], heap[(index - 1) // 2] = heap[(index - 1) // 2], heap[index]
        index = (index - 1) // 2
        if index <= 0:
            break


# 如何利用堆进行排序
def heapSort(heap: List[int]) -> None:
    if heap is None or len(heap) < 2:
        return
    # 对 heap 变成堆
    n = len(heap)
    for i in range(n):
        print(i, heap[i])
        if i == 7:
            print(i)
            pass
        heapInsert(heap, i)

        print(heap)
    print(heap)
    size = n
    heap[0], heap[size - 1] = heap[size - 1], heap[0]
    size -= 1
    while size > 0:
        max_heapify(heap, 0, size)
        heap[0], heap[size - 1] = heap[size - 1], heap[0]
        size -= 1


def list2max_heap(heap: List[int]) -> None:
    if heap is None or len(heap) < 2:
        return
    # 对 heap 变成堆
    n = len(heap)
    for i in range(n):
        # print(i, heap[i])
        heapInsert(heap, i)
        # print(heap)


def heap_pop_max(heap: List[int]) -> int:
    if len(heap) == 0:
        return -1
    heap[0], heap[-1] = heap[-1], heap[0]
    max_heapify(heap, 0, len(heap) - 1)
    return heap.pop()


def heap_pop_max2(heap: List[int]) -> int:
    if len(heap) == 0:
        return -1
    heap[0], heap[-1] = heap[-1], heap[0]
    heapify_max2(heap, 0, len(heap) - 1)
    return heap.pop()

def heap_pop_min(heap: List[int]) -> int:
    if len(heap) == 0:
        # Raises IndexError if list is empty or index is out of range.
        raise IndexError("list is empty or index is out of range")
    heap[0], heap[-1] = heap[-1], heap[0]
    heapify_min(heap, 0, len(heap) - 1)
    return heap.pop()

def heap_push_max(heap: List[int], num: int):
    index = len(heap)
    heap.append(num)
    if index <= 0:
        return
    while heap[index] > heap[(index - 1) // 2]:
        # while 循环的终止条件是当前节点比它的父节点小
        # left 节点刚好为 奇数
        # right 节点刚好为 偶数
        # 因此 (left - 1)//2 == (right - 1)//2
        heap[index], heap[(index - 1) // 2] = heap[(index - 1) // 2], heap[index]
        index = (index - 1) // 2
        if index <= 0:
            break
def heap_push_min(heap: List[int], num: int):
    index = len(heap)
    heap.append(num)
    if index <= 0:
        return
    while heap[index] < heap[(index - 1) // 2]:
        # while 循环的终止条件是当前节点比它的父节点大
        # left 节点刚好为 奇数
        # right 节点刚好为 偶数
        # 因此 (left - 1)//2 == (right - 1)//2
        heap[index], heap[(index - 1) // 2] = heap[(index - 1) // 2], heap[index]
        index = (index - 1) // 2
        if index <= 0:
            break

# heap实际上在python中可以通过list实现
def max_heapify(heap: List[int], index: int, heapSize: int) -> None:
    # 主要思想，heap中 0 和 (index-1)之间为最大堆，然后添加index的值，使其重新成为最大堆
    # 要调整的节点的左孩子节点
    left = 2 * index + 1

    # 0到heapSize-1,是大根堆，所以当left等于或者大于heapSize的时候，说明index对应的节点就是叶子节点
    while left < heapSize:
        # 获取更大的叶子节点
        right = left + 1
        if right >= heapSize:
            larger = left
        else:
            larger = right if heap[right] > heap[left] else left
        # 叶子节点和父节点进行比较
        largest = larger if heap[larger] > heap[index] else index

        if largest == index:
            # 如果当前节点比它的左右子节点都大的话，就没有必要再进行交换了
            break
        else:
            heap[largest], heap[index] = heap[index], heap[largest]

        index = largest
        left = index * 2 + 1


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


def heapify_min(heap: List[int], index: int, heapSize: int) -> None:
    left = index * 2 + 1
    while left < heapSize:
        # 1 左右两节点比较, 获取更小的叶子节点
        right = left + 1
        if right >= heapSize:
            smaller = left
        else:
            smaller = right if heap[right] < heap[left] else left
        # 2 子节点和父节点进行比较
        smallest = index if heap[index] < heap[smaller] else smaller
        if smallest == index:
            # 没有必要进行交换
            break
        else:
            # 3 交换子节点和父节点的位置
            heap[index], heap[smallest] = heap[smallest], heap[index]
        index = smallest
        left = index * 2 + 1


def buildMaxHeap(heap: List[int]) -> None:
    n = len(heap)
    for i in range(n // 2, -1, -1):
        # 自顶向下
        heapify_max2(heap, i, n)


def buildMinHeap(heap: List[int]) -> None:
    n = len(heap)
    for i in range(n // 2, -1, -1):
        # 自顶向下
        heapify_min(heap, i, n)


def maxheap_test():
    heap1 = [1, 3, 5, 6, 2, 5, 7, 9]
    print(heap1)
    list2max_heap(heap1)
    print(heap1)
    pop_item = heap_pop_max2(heap1)
    print(pop_item)
    print(heap1)
    heap_push_max(heap1, pop_item)
    print(heap1)


def maxheap_test2():
    heap2 = [1, 3, 5, 6, 2, 5, 6, 0, -1, 23, 100, 7, 9, 9]
    buildMaxHeap(heap2)
    print(heap2)
    res = []
    while heap2:
        item = heap_pop_max2(heap2)
        res.append(item)
    print(res[::-1])


def minheap_test():
    # 测试构建最小堆功能
    heap1 = [1, 2, 3, 4, 5, 6, 7, 9]
    heap2 = heap1[::-1]
    print(heap2)
    buildMinHeap(heap1)
    buildMinHeap(heap2)
    print(heap1)
    print(heap2)
    # 测试 最小堆 pop
    res = []
    while heap2:
        item = heap_pop_min(heap2)
        res.append(item)
    print(res[::])

    # 测试构建最小堆 push
    heap2 = [9, 7, 6, 5, 4, 3, 2, 1]
    heap3 = []
    for i in range(len(heap2)):
        heap_push_min(heap3, heap2[i])
        print(heap3)




if __name__ == '__main__':
    minheap_test()
