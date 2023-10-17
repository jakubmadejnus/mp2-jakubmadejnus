"""
Problem: Implement Heapify for MinHeap

Description:
Implement the heapify method for the `MinHeap` class. 
This method should transform an arbitrary array into a valid min heap, ensuring the smallest element is at the root and both the left and right children of any node are larger than the node.

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
        self.heapify()  # Calling heapify upon initialization

    def sift_down(self, n, idx):
        smallest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2

        # Check if the left child exists and is less than the current smallest
        if left < n and self.heap[left] < self.heap[smallest]:
            smallest = left

        # Check if the right child exists and is less than the current smallest
        if right < n and self.heap[right] < self.heap[smallest]:
            smallest = right

        # If the smallest is not the current node, swap and continue sifting down
        if smallest != idx:
            self.heap[idx], self.heap[smallest] = self.heap[smallest], self.heap[idx]
            self.sift_down(n, smallest)

    def heapify(self):
        # Last non-leaf node (parent of the last element) is at (n//2) - 1
        start_idx = len(self.heap) // 2 - 1

        # Go up the heap, ensuring min-heap property is maintained
        for i in range(start_idx, -1, -1):
            self.sift_down(len(self.heap), i)

