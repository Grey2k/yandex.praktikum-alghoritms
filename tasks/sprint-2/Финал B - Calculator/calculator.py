"""
-- ПРИНЦИП РАБОТЫ --
Мы получаем на вход выражение, записанное в польской нотации, записываем его в список и итерируемся слева направо.
Если мы встречаем число - то добавляем его в буфер (стек)

Если операнд то мы в нужной последовательности сперва извлекаем числа из стека и
производим над ними операцию, результат сохраняем в стек и продолжаем разбор выражения

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Решение выполнено в соответствии с заданными условиями и подтверждено юнит-тестами

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Так как мы работаем со стеком на основе массива вставка и получение элемента с конца массива стоит O(1)

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Стек, содержащий n элементов, занимает O(n) памяти

-- ID успешной посылки --
48888874
"""


class Stack:
    def __init__(self, array=None):
        self.stack = [] if array is None else array

    def pop(self):
        return self.stack.pop()

    def push(self, value):
        self.stack.append(value)
        return self.stack

    def is_empty(self):
        return len(self.stack) == 0


def is_int(char: str):
    return char.lstrip('+-').isnumeric()


def main():
    try:
        sequence = input().split()
    except EOFError:
        sequence = []

    stack = Stack()

    for char in sequence:
        if is_int(char):
            stack.push(int(char))
            continue

        second = stack.pop()
        first = stack.pop()

        # operator cases
        if char == '+':
            stack.push(first + second)
            continue

        if char == '-':
            stack.push(first - second)
            continue

        if char == '*':
            stack.push(first * second)
            continue

        if char == '/':
            stack.push(first // second)
            continue

    print(0 if stack.is_empty() else stack.pop())


if __name__ == '__main__':
    main()
