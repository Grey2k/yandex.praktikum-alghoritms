class QueueSized:
    def __init__(self, max_size: int):
        self.queue = [None] * max_size
        self.max_size = max_size
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def pop(self):
        if self.is_empty():
            return None
        value = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.size -= 1
        return value

    def peek(self):
        if self.is_empty():
            return None
        value = self.queue[self.head]
        return value

    def push(self, value):
        if self.size != self.max_size:
            self.queue[self.tail] = value
            self.tail = (self.tail + 1) % self.max_size
            self.size += 1
            return

        raise IndexError('Queue is full')


def main():
    length = int(input())
    size = int(input())
    queue = QueueSized(size)

    for _ in range(length):
        cmd = input().strip().split()

        if cmd[0] == 'peek':
            print(queue.peek())
            continue

        if cmd[0] == 'size':
            print(queue.size)
            continue

        if cmd[0] == 'pop':
            print(queue.pop())
            continue

        if cmd[0] == 'push':
            try:
                queue.push(int(cmd[1]))
            except IndexError:
                print('error')


if __name__ == '__main__':
    main()
