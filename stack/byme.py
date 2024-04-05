class Stack:
    def __init__(self, capacity: int):
        # Write your code here.
        self.capacity = capacity
        self._top = -1
        self.stack = []

    def push(self, num: int) -> None:
        # Write your code here.
        if self._top + 1 == self.capacity:
            # print("Stack is full !")
            return

        self.stack.append(num)
        self._top += 1

    def pop(self) -> int:
        # Write your code here.
        if self._top == -1:
            return -1  # stack is empty
        self._top -= 1

        # print the top element
        return self.stack[self._top + 1]
        # decrease the size of the array

    def top(self) -> int:
        if self._top == -1:
            return -1  # stack is empty

        return self.stack[self._top]

    def isEmpty(self) -> int:
        # Write your code here.
        return 1 if self._top == -1 else 0

    def isFull(self) -> int:
        # Write your code here.
        return 1 if self._top + 1 == self.capacity else 0


"""
2 6
1 1
1 2
2
3
4
5
"""

"""
5 10
4
4
4
4
4
4
4
4
4
4
"""


def main():
    input = """2 6
1 1
1 2
2
3
4
5"""

    input = input.split("\n")
    N, M = input[0].split(" ")
    N, M = int(N), int(M)

    s = Stack(N)

    for opr in range(1, M + 1):
        inp = input[opr]

        if len(inp) > 1:
            # input
            _, num = inp.split(" ")
            num = int(num)

            s.push(num)
            continue

        if inp == "2":
            print(s.pop())
        elif inp == "3":
            print(s.top())
        elif inp == "4":
            print(s.isEmpty())
        elif inp == "5":
            print(s.isFull())


main()
