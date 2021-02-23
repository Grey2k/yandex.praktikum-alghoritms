class StackMax:
    def __init__(self, array=None):
        self.stack = [] if array is None else array

    def pop(self):
        return self.stack.pop()

    def push(self, value):
        self.stack.append(value)
        return self.stack

    def get_max(self):
        return max(self.stack)


def main():
    length = int(input())
    stack = StackMax()

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
