# 最小栈 https://leetcode.cn/problems/min-stack/solutions/9036/min-stack-fu-zhu-stackfa-by-jin407891080/?envType=study-plan-v2&envId=top-100-liked
# 最小栈

class MinStack:
    # 最小栈利用栈的先进后出的原理，将在栈偏栈顶的位置的最小值放在最小栈的上面，保证两件事
    # 1 push 时，将更小的最小值放在最小栈的栈顶，保证查询最小值时正确
    # 2 pop 时，也是因为更小的值是在后面push进去的，因此更小值能够更早pop出去
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # 注意<= ，保证相同的最小值能够进入最小栈，从而在pop的时候保证正确弹出最小栈中的值
        # 举例
        # stack     0 1 0
        # minStack  0
        # 第一次pop时，minStack为空了
        # stack     [0 1]
        # minStack  []
        # 获取最小值时，就会出错
        # 注意初始minStack为空的情况
        # 注意初始minStack为空的情况
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)

    def pop(self) -> None:
        # 确认 minStack 是否需要pop
        if self.stack.pop() == self.minStack[-1]:
            self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

