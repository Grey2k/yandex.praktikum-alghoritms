def merge(arr, left, mid, right):
    first = arr[left:mid]
    second = arr[mid:right]

    if len(second) == 0:
        return first

    if len(first) == 0:
        return second

    result = [0] * (len(first) + len(second))

    l, r, k = 0, 0, 0

    while l < len(first) and r < len(second):
        # выбираем, из какого массива забрать минимальный элемент
        if first[l] <= second[r]:
            result[k] = first[l]
            l += 1
        else:
            result[k] = second[r]
            r += 1
        k += 1

    # Если один массив закончился раньше, чем второй, то
    # переносим оставшиеся элементы второго массива в результирующий
    while l < len(first):
        result[k] = first[l]  # перенеси оставшиеся элементы left в result
        l += 1
        k += 1

    while r < len(second):
        result[k] = second[r]  # перенеси оставшиеся элементы right в result
        r += 1
        k += 1

    return result


def merge_sort(arr, left, right):
    if (right - left) <= 1:
        return

    mid = (right + left) // 2
    merge_sort(arr, left, mid)
    merge_sort(arr, mid, right)

    merged = merge(arr, left, mid, right)

    m = 0
    for i in range(left, right):
        arr[i] = merged[m]
        m += 1
