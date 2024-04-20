def main():
    while True:
        try:
            count = eval(input().strip())
            for i in range(count):
                line = input().strip()
                line_list = line.split(' ')
                a, b = map(int, line_list)
                print(a + b)

        except EOFError:
            break


if __name__ == '__main__':
    main()
