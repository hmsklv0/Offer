# 队列：先进先出
# 栈：先进后出


class CQueue:
    def __init__(self):
        # 定义两个栈
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, value: int) -> None:
        self.stack1.append(value)

    def deleteHead(self) -> int:
        # 利用stack2 存储预想的队列头部，等到stack2中没有元素时，将 stack1 中的元素以 pop 的形式压入 stack2 中
        queue_len1 = len(self.stack1)
        queue_len2 = len(self.stack2)
        queue_len = queue_len1 + queue_len2

        # 01 若队列中没有元素，则返回 -1
        if queue_len == 0:
            return -1
        # 02 条件判断 等到stack2中没有元素时，将 stack1 中的元素以 pop 的形式压入 stack2 中
        if queue_len2 == 0:
            for i in range(queue_len1):
                self.stack2.append(self.stack1.pop())
        # 队列头部 pop
        return self.stack2.pop()


def main():
    test = CQueue()

    print(test.deleteHead())
    print(test.appendTail(5))
    print(test.appendTail(2))
    print(test.deleteHead())
    print(test.deleteHead())

if __name__ == '__main__':
    main()

# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()