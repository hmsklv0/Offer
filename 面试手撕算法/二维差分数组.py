import copy

# 二维差分数组
# 需要预留出索引为 0 的行和列，方便后续计算前缀和时进行计算
N = 5
diff = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
a = copy.deepcopy(diff)


def inset(x1, y1, x2, y2, c):
    # diff[x2 + 1][y2 + 1] += c
    # 避免之后累计减去两次 c
    diff[x1][y1] += c
    diff[x1][y2 + 1] -= c
    diff[x2 + 1][y1] -= c
    diff[x2 + 1][y2 + 1] += c


def print_(array: list[list[int]]):
    for index in range(N):
        print(array[index])


inset(1, 1, 3, 3, 1)
inset(2, 2, 4, 4, 1)

for i in range(1, N + 1):
    for j in range(1, N + 1):
        a[i][j] = diff[i][j] + a[i - 1][j] + a[i][j - 1] - a[i - 1][j - 1]

print_(diff)
print()
print_(a)

# 一维差分数组
a1 = [0 for i in range(N)]
diff1 = [0 for i in range(N)]


def insert1(x, y, c):
    diff1[x] += c
    diff1[y + 1] -= c


insert1(1, 3, 1)
for i in range(1, N):
    a1[i] = diff1[i] + a1[i - 1]
print(a1)
