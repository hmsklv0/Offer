链接: https://leetcode.cn/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/?envType=study-plan&id=lcof&plan=lcof&plan_progress=f6t2nyj

#### 优秀解法

```python
class CQueue:

    def __init__(self):
        self.A, self.B = [], []
    
    def appendTail(self, value: int) -> None:
        self.A.append(value)
    
    def deleteHead(self) -> int:
        if self.B:
            return self.B.pop()
        if not self.A:
            return -1
        while self.A:
            self.B.append(self.A.pop())
        return self.B.pop()



# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
```

包含min函数的栈 优秀题解

https://leetcode.cn/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/solutions/100368/mian-shi-ti-09-yong-liang-ge-zhan-shi-xian-dui-l-2/?orderBy=hot