class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class StackList:
    def __init__(self, array=None):
        self.stack = [] if array is None else array

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def push(self, value):
        self.stack.append(value)
        return self.stack


class StackMaxEffective:
    def __init__(self):
        self.stack = None
        self.max = StackList()

    def pop(self):
        if self.stack is None:
            raise IndexError('Stack is Empty')

        head = self.stack
        self.stack = head.next

        try:
            if self.max.peek() == head.value:
                self.max.pop()
        except IndexError:
            pass

        return head

    def push(self, value):
        node = Node(value, next=self.stack)
        self.stack = node

        try:
            if self.max.peek() <= node.value:
                self.max.push(node.value)
        except IndexError:
            self.max.push(node.value)

        return node

    def get_max(self):
        try:
            return self.max.peek()
        except IndexError:
            return None


def main():
    length = int(input())
    stack = StackMaxEffective()

    for _ in range(length):
        cmd = input().strip().split()

        if cmd[0] == 'get_max':
            try:
                print(stack.get_max())
            except ValueError:
                print(None)

            continue

        if cmd[0] == 'pop':
            try:
                stack.pop()
            except IndexError:
                print('error')

            continue

        if cmd[0] == 'push':
            stack.push(int(cmd[1]))


if __name__ == '__main__':
    main()
