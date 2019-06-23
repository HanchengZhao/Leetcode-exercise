# use 2 stack to store input and output, always use the output stack to do the
# peek and pop operations. When the output stack is empty, push all the elements
# from the input array to the output array


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.input.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self.output) == 0:
            while len(self.input) != 0:
                self.output.append(self.input.pop())
        return self.output.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.output) == 0:
            while len(self.input) != 0:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.input) == 0 and len(self.output) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
