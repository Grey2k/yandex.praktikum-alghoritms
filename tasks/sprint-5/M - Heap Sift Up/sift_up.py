def sift_up(heap: list, idx: int) -> int:
    if idx == 1:
        return idx

    parent_idx = idx // 2

    if heap[parent_idx] < heap[idx]:
        heap[idx], heap[parent_idx] = heap[parent_idx], heap[idx]
        idx = sift_up(heap, parent_idx)

    return idx
