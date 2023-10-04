from typing import List
from heapq import heappush, heappop

def find_Kth_smallest(nums: List[int], k: int) -> int:  
    max_heap = []
    for i in range(k):
        heappush(max_heap, -nums[i])

    for i in range(k, len(nums)):
        if -nums[i] > max_heap[0]:
            heappop(max_heap)
            heappush(max_heap, -nums[i])

    return -max_heap[0]


def test_find_Kth_smallest():
    # Basic test cases
    assert find_Kth_smallest([1, 5, 12, 2, 11, 5], 3) == 5
    assert find_Kth_smallest([1, 5, 12, 2, 11, 5], 4) == 5
    assert find_Kth_smallest([5, 12, 11, -1, 12], 3) == 11

    # Large test case for efficiency
    nums = [i for i in range(10**7, 0, -1)]
    k = 5000000
    assert find_Kth_smallest(nums, k) == k

    print("All test cases pass")
