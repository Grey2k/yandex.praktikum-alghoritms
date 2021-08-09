def sift_down(heap: list, idx: int) -> int:
    left_index = 2 * idx
    right_index = 2 * idx + 1
    heap_size = (len(heap) - 1)

    # no children
    if heap_size < left_index:
        return idx

    # has left & right children
    if right_index <= heap_size and heap[left_index] < heap[right_index]:
        index_largest = right_index
    else:
        index_largest = left_index

    if heap[idx] < heap[index_largest]:
        heap[idx], heap[index_largest] = heap[index_largest], heap[idx]
        idx = sift_down(heap, index_largest)

    return idx
