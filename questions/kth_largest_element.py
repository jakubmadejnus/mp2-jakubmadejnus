"""
Kth Largest Number in a Stream

Problem Statement:
Design a class that can efficiently find the Kth largest element in a stream of numbers.

Requirements:
1. The class should have a constructor which accepts an integer array containing initial numbers from the stream and an integer ‘K’.
2. The class should have a function add(int num) which will store the given number and return the Kth largest number.

Example:
Input: [3, 1, 5, 12, 2, 11], K = 4
1. Calling add(6) should return '5'.
2. Calling add(13) should return '6'.
3. Calling add(4) should still return '6'.

Note: 
The stream can contain duplicate numbers.

Notes:
    - Recall your approach for `kth_smallest_element.py`

Tags:
    - Sorting
    - Priority Queue
    - Google Interview Question

"""

import heapq

class KthLargest:
    def __init__(self, nums, k):
        self.k = k
        self.minHeap = []
        for num in nums:
            self.add(num)

    def add(self, num):
        heapq.heappush(self.minHeap, num)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
    
