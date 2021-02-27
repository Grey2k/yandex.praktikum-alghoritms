"""
-- ПРИНЦИП РАБОТЫ --
Я реализовал дек на кольцевом буфере, на основе предложенного теоретического решения для очереди и доработал его
сложности возникли в том что приходилось следить за концом и началом, в итоге опытным путем
нашел просутю формулу по расчету хвоста через голову и наоборот

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Мы всегда идем по массиву и считаем счетчик для контроля переполненеия, все проверено написанными юнит-тестами

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Добавление в дек стоит O(1), потому что мы всегда работаем с массивом по индексу (доступ по индексу O(1))
Извлечение аналогично

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Дек, содержащий n элементов, занимает O(n) памяти. + значения счетчиков, в итоге сложность O(n)

-- ID успешной посылки --
48890177
"""


class Deck:
    SIZE_LIMIT = 1000

    def __init__(self, max_size=0):
        self.max_size = max_size if 0 <= max_size <= Deck.SIZE_LIMIT else Deck.SIZE_LIMIT
        self.deck = [None] * self.max_size

        self.head = 0
        self.tail = 0
        self.size = 0

    def push_back(self, item):
        if self.size == self.max_size:
            raise OverflowError('Deck is full')

        self.tail = (self.tail - 1) % self.max_size
        self.size += 1

        self.head = (self.tail + self.size - 1) % self.max_size
        self.deck[self.tail] = item

    def pop_back(self):
        if self.size == 0:
            raise ValueError('Deck is empty')

        item = self.deck[self.tail]

        self.tail = (self.tail + 1) % self.max_size
        self.size -= 1

        self.head = (self.tail + self.size - 1) % self.max_size
        return item

    def push_front(self, item):
        if self.size == self.max_size:
            raise OverflowError('Deck is full')

        self.head = (self.head + 1) % self.max_size
        self.size += 1

        self.tail = (self.head - self.size + 1) % self.max_size
        self.deck[self.head] = item

    def pop_front(self):
        if self.size == 0:
            raise ValueError('Deck is empty')

        item = self.deck[self.head]

        self.head = (self.head - 1) % self.max_size
        self.size -= 1

        self.tail = (self.head - self.size + 1) % self.max_size
        return item


CMD_PUSH_FRONT = 'push_front'
CMD_PUSH_BACK = 'push_back'
CMD_POP_FRONT = 'pop_front'
CMD_POP_BACK = 'pop_back'


def main():
    commands = int(input())
    deck_size = int(input())

    deck = Deck(deck_size)
    for _ in range(commands):
        cmd = input().strip().split()

        if cmd[0] == CMD_POP_FRONT:
            try:
                print(deck.pop_front())
            except ValueError:
                print('error')
            continue

        if cmd[0] == CMD_POP_BACK:
            try:
                print(deck.pop_back())
            except ValueError:
                print('error')
            continue

        if cmd[0] == CMD_PUSH_FRONT:
            try:
                deck.push_front(int(cmd[1]))
            except OverflowError:
                print('error')
            continue

        if cmd[0] == CMD_PUSH_BACK:
            try:
                deck.push_back(int(cmd[1]))
            except OverflowError:
                print('error')


if __name__ == '__main__':
    main()
