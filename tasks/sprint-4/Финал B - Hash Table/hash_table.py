"""
-- ПРИНЦИП РАБОТЫ --
В представленной реализации структуры данных HashTable я задаю максимальное возможное кол-во бакетов по условии задачи
для вычисления бакета использую остаток от деления от максимума (так как все ключи integer) далее определив бакет
- храню в нем пары (key, value). Для дополнительной оптимизации по скорости - ключи в бакете удаляются,
после замены с последним элементом чтобы исключить сдвиг в массиве (спасибо за подсказку!)

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Решение проверено написанными юнит-тестами

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
У нас определены граничные условия (размер и диапазон ключей N)
Временная сложность O(Const) , где Const в худшем случае N / SIZE = 10^4

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
В Худшем случае мы будем иметь O(N) где N - кол-во ключей

-- ID успешной посылки --
50346119
"""
import sys

MAX_SIZE = 99991  # простое число меньше 10^5


class HashTable:
    def __init__(self, max_size=MAX_SIZE):
        self.max_size = max_size
        self.buckets = tuple(([] for _ in range(max_size)))

    @staticmethod
    def __calc_hash(key):
        return key

    def __get_bucket(self, key):
        return key % self.max_size

    def get(self, key):
        bucket = self.buckets[self.__get_bucket(key)]

        if len(bucket) == 0:
            return None

        for value in bucket:
            if value[0] == key:
                return value[1]

        return None

    def put(self, key, value):
        bucket = self.buckets[self.__get_bucket(key)]

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
        bucket = self.buckets[self.__get_bucket(key)]
        length = len(bucket)

        if length == 0:
            return None

        for i in range(len(bucket)):
            if bucket[i][0] == key:
                if length == 1 or i == (length - 1):
                    return bucket.pop()[1]

                bucket[i], bucket[-1] = bucket[-1], bucket[i]
                return bucket.pop()[1]
        return None


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
