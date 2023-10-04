from questions.min_heapify import MinHeap

def is_valid_min_heap(arr):
    n = len(arr)
    for i in range(n):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[i] > arr[left]:
            return False
        if right < n and arr[i] > arr[right]:
            return False
    return True

import random
import time 

def test_heapify():
    # Test Case 1
    heap = MinHeap([3, 1, 4, 1, 5, 9, 2, 6])
    heap.heapify()
    assert is_valid_min_heap(heap.heap)

    # Test Case 2
    heap = MinHeap([5, 3, 8, 5, 2, 9, 10])
    heap.heapify()
    assert is_valid_min_heap(heap.heap)

    # Test Case 3: Large input for efficiency
    nums = [i for i in range(10000, 0, -1)]
    heap = MinHeap(nums)
    heap.heapify()
    assert is_valid_min_heap(heap.heap)

    # Test Case 4: Edge Cases
    heap = MinHeap([])
    heap.heapify()
    assert is_valid_min_heap(heap.heap)

    heap = MinHeap([5])
    heap.heapify()
    assert is_valid_min_heap(heap.heap)

    sizes = [10**5, 10**6, 10**7]

    for size in sizes:
        # Generating large random lists
        nums = [random.randint(1, size) for _ in range(size)]
        
        heap = MinHeap(nums)
        
        start_time = time.time()
        heap.heapify()
        end_time = time.time()

        assert is_valid_min_heap(heap.heap)

        print(f"Heapify for size {size} took {end_time - start_time:.5f} seconds.")
