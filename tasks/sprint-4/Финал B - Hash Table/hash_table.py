"""
-- ПРИНЦИП РАБОТЫ --
В представленной реализации структуры данных HashTable я задаю максимальное возможное кол-во бакетов по условии задачи
для вычисления бакета использую остаток от деления от максимума (так как все ключи integer) далее определив бакет
- храню в нем пары (key, value). Для дополнительной оптимизации по скорости - ключи в бакете не удаляются,
а удаляются только значения (думаю что это допустимо так как мы инкапсулируем реальное поведение объекта,
хотя и жертвуем памятью)

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Решение проверено написанными юнит-тестами

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
У нас определены граничные условия (размер и диапазон ключей N)
Временная сложность O(Const) , где Const в худшем случае N / SIZE = 10^4

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
В Худшем случае мы будем иметь O(N) где N - кол-во ключей

-- ID успешной посылки --
50312048
"""
import sys

MAX_SIZE = 10 ** 5


class HashTable:
    def __init__(self, max_size=MAX_SIZE):
        self.max_size = max_size
        self.buckets = tuple(([] for _ in range(max_size)))

    def __calc_hash(self, key):
        return key % self.max_size

    def get(self, key):
        bucket = self.buckets[self.__calc_hash(key)]

        if len(bucket) == 0:
            return None

        for value in bucket:
            if value[0] == key:
                return value[1]

        return None

    def put(self, key, value):
        bucket = self.buckets[self.__calc_hash(key)]

        if len(bucket) == 0:
            bucket.append((key, value))
            return

        for i in range(len(bucket)):
            if bucket[i][0] == key:
                if bucket[i][1] != value:
                    bucket[i] = (key, value)
                return

        bucket.append((key, value))
        return

    def delete(self, key):
        bucket = self.buckets[self.__calc_hash(key)]
        value = None

        if len(bucket) == 0:
            return value

        for i in range(len(bucket)):
            if bucket[i][0] == key:
                if bucket[i][1] is not None:
                    value = bucket[i][1]
                    bucket[i] = (key, None)
                return value
        return value


CMD_GET = 'get'
CMD_PUT = 'put'
CMD_DELETE = 'delete'


def main():
    n = int(input())

    hash_table = HashTable()

    for _ in range(n):
        args = sys.stdin.readline().strip().split()

        if args[0] == CMD_GET:
            print(hash_table.get(int(args[1])))

        elif args[0] == CMD_PUT:
            hash_table.put(int(args[1]), int(args[2]))

        elif args[0] == CMD_DELETE:
            print(hash_table.delete(int(args[1])))

        else:
            raise RuntimeError(f'Unknown Command: {args[0]}')


if __name__ == '__main__':
    main()
