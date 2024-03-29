"""
-- ПРИНЦИП РАБОТЫ --
Сперва мы создаем индекс - хеш-таблица с элементами (id документа, кол-во вхождений),
далее считаем релевантность по каждому запросу и сортируем результат

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Задача соответствует условиям, работа проверена с написанными юнит-тестами

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Временная сложность O(K x I x L) - где
K - кол-во уникальных слов в индексе (суммарное),
I - кол-во повторений каждого слова в докуменах
L - Кол-во уникальных слов в запросах (суммарное)


-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Пространственная сложность O(K * I) -
где K - суммарное кол-во уникальных слов в документах
где I - кол-во повторений каждого слова в докуменах


-- ID успешной посылки --
50345603
"""
import sys
from collections import Counter
from heapq import nsmallest

LIMIT = 5


def main():
    n = int(input())

    index = {}
    for idx in range(n):
        counter = Counter(sys.stdin.readline().strip().split())
        for word in counter:
            word_index = index.get(word)
            index_el = (idx + 1, counter[word])
            if word_index is None:
                index[word] = [index_el]
            else:
                index[word].append(index_el)

    q = int(input())

    for _ in range(q):
        query = sys.stdin.readline().strip().split()
        docs = search_engine(query, index)

        if len(docs) > 0:
            print(' '.join(map(str, docs)))


def search_engine(query, index):
    relevant_results = {}
    for word in set(query):
        index_item = index.get(word)
        if index_item is None:
            continue

        for doc_idx, count in index_item:
            relevance = relevant_results.get(doc_idx)
            if relevance is None:
                relevant_results[doc_idx] = count
            else:
                relevant_results[doc_idx] += count

    return [result[0] for result in nsmallest(LIMIT, relevant_results.items(), key=lambda item: (-item[1], item[0]))]


if __name__ == '__main__':
    main()
