import collections


def func1():
    original_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    sorted_list = sorted(original_list)
    print("Original List:\t", original_list)
    print("Sorted List:\t", sorted_list)


def func2():
    original_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    original_list.sort()
    print("Sorted List:", original_list)


def func3():
    """
        [None]和[]在Python中是不同的：
        [None]是一个包含一个元素的列表，该元素是None。即使列表只包含一个元素，它仍然是一个列表。
        []是一个空列表，不包含任何元素。
    """
    print(len([None]))


def func4():
    # 测试counter对象
    s = "aaabbb"
    count = collections.Counter(s)
    count.update({"a": -1, "c": -1})
    print(count)


def func5():
    # 测试矩阵列输出
    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    print([i[0] for i in matrix])


def func6():
    # 测试for循环的逆序输出
    for i in range(3, -2, -1):
        print(i)


def func7():
    for i in range(3):
        print(i)
    print(i)


def func8():
    list1 = [1]
    print(list1[0:0], list1[1:])
    list2 = [0, 1]
    print(list2[0:1], list2[2:])
    list3 = [0, 1, 2]
    print(list3[0:1], list3[2:])


def func9():
    list1 = [1, 2, 3]
    print(list1.pop())


def func10():
    list1 = [1, 2, 3]
    print(id(list1))
    list2 = [4, 5, 6]
    list1.extend(list2)
    print(list1)
    print(id(list1))


def func11():
    # list浅层copy
    list1 = [[]] * 3
    list3 = [None] * 3
    list2 = [[] for i in range(3)]
    print(list3)
    for i in [0, 1, 2]:
        list1[0].append(i)
        list2[0].append(i)
        print(id(list1[i]))
        print(id(list2[i]))
    print(list1)
    print(list2)


def func12():
    str1 = "aaaa"
    str2 = str1 * 3
    print(str2)


def func13():
    list1 = [1, 2, 3]
    list2 = []
    list2.append(list1)
    print(list2)
    list1.append(4)
    list2.append(list1)
    print(list2)


def func14():
    # 测试二维数组生成
    board = [[0, 0], [0, 0]]
    visited = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
    print(visited)


def func15():
    # 测试字符串连接生成
    list1 = ['.' for i in range(3)]
    list2 = ['.' * 3]
    print(list1)
    print(list2)

    #   ['.', '.', '.']
    #   ['...']


def func16():
    str1 = "abcd"
    list1 = ['a', 'b', 'c', 'd']
    str1[0] = 'b'
    list1[0] = 'b'
    # 提示: 类 'str' 未定义 '__setitem__'，所以不能对其实例使用 '[]' 运算符


def func17():
    for i in range(3):
        print(i)
        if i == 1:
            i -= 1
# 0
# 1
# 2

func17()
# func15()
# func7()
# func8()
# func11()
