"""
Problem: Implement Heapify for MinHeap

Description:
Implement the heapify method for the `MinHeap` class. This method should transform an arbitrary array into a valid min heap, ensuring the smallest element is at the root and both the left and right children of any node are larger than the node.

Function Signature:
def heapify(self) -> None:

Inputs:
    - self.heap: A list of integers representing the current state of the heap. The heap may not initially satisfy the min heap property.

Outputs:
    - No explicit return value (None). The function modifies the `self.heap` in-place to form a min heap.

Examples:
1. Input: Initial heap = [3, 1, 4, 1, 5, 9, 2]
   After heapify: heap = [1, 1, 2, 3, 5, 9, 4]
   Explanation: The smallest number, 1, is moved to the root, and subsequent numbers are adjusted to maintain the min heap property.

2. Input: Initial heap = [10, 20, 15, 17, 25]
   After heapify: heap = [10, 17, 15, 20, 25]
   Explanation: The array is adjusted to satisfy the min heap property without any unnecessary swaps.

Notes:
    - The core idea of the heapify process is to ensure the root node is the smallest in the heap and recursively ensure this property for all child nodes.
    - An effective approach is to start from the last non-leaf node and move upwards, repeatedly ensuring the heap property is maintained at every node.
    - Internal helper functions may be needed for operations like sifting down an element to its correct position.

Tags:
    - Heaps
    - In-place algorithms
"""

class MinHeap:
    def __init__(self, arr=None):
        self.heap = arr or []

    def heapify(self):
        pass
