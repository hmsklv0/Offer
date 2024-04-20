import sys


def func1():
    for line in sys.stdin:
        input_str = line
        input_list = input_str.split(' ')
        a, b = int(input_list[0]), int(input_list[1])
        print(a + b)


def func2():
    while True:
        try:
            input_str = input().strip()
            if not input_str:
                break  # 如果输入为空，则退出循环
            a, b = map(int, input_str.split())
            print(a + b)
        except EOFError:
            break  # 如果到达文件末尾，则退出循环


def main():
    func1()


if __name__ == '__main__':
    main()
