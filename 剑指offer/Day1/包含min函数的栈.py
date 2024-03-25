class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        # 压入元素
        self.stack1.append(x)
        # 如果辅助栈 stack2 为空或者 stack2 的栈尾元素，即最小元素小于当前 x, 则添加 x 元素到该栈中
        if not self.stack2 or self.stack2[-1] >= x:
            self.stack2.append(x)

    def pop(self) -> None:
        # 如果弹出的恰好是最小元素，stack2也要弹出该元素
        if self.stack1.pop() == self.stack2[-1]:
            self.stack2.pop()

    def top(self) -> int:
        # 返回栈顶元素
        return self.stack1[-1]

    def min(self) -> int:
        # 返回辅助栈的栈尾元素
        return self.stack2[-1]





# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()