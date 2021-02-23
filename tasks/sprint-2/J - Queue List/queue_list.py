class Node:
    def __init__(self, value, next_node=None, prev=None):
        self.value = value
        self.next_node = next_node
        self.prev = prev


class QueueList:
    def __init__(self):
        self.queue = None
        self.size = 0
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.size == 0

    def size(self):
        return self.size

    def get(self):
        if self.head is None:
            raise IndexError('Queue is empty')

        self.size -= 1

        head = self.head
        if isinstance(head, Node) and isinstance(head.prev, Node):
            self.head = head.prev
            self.head.next_node = None

        if self.is_empty():
            self.head = None
            self.tail = None

        return head.value

    def put(self, value):
        node = Node(value, next_node=self.tail)
        self.size += 1

        if self.head is None and self.tail is None:
            self.head = node
            self.tail = node
            return

        if isinstance(self.tail, Node):
            self.tail.prev = node

        self.tail = node


def main():
    length = int(input())
    queue = QueueList()

    for _ in range(length):
        cmd = input().strip().split()

        if cmd[0] == 'get':
            try:
                print(queue.get())
            except IndexError:
                print('error')

            continue

        if cmd[0] == 'size':
            print(queue.size)
            continue

        if cmd[0] == 'put':
            queue.put(int(cmd[1]))


if __name__ == '__main__':
    main()
