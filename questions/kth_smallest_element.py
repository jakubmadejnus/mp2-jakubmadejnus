"""
Problem: Find the Kth Smallest Number in an Unsorted Array

Description:
Given an unsorted array of numbers, the task is to find the Kth smallest number in it.
Note that it refers to the Kth smallest number in the sorted order, not the Kth distinct element.

Function Signature:
def find_Kth_smallest(nums: List[int], k: int) -> int:

Examples:
1. Input: [1, 5, 12, 2, 11, 5], K = 3
   Output: 5
   Explanation: The 3rd smallest number is '5', as the first two smaller numbers are [1, 2].
   
2. Input: [1, 5, 12, 2, 11, 5], K = 4
   Output: 5
   Explanation: The 4th smallest number is '5', as the first three small numbers are [1, 2, 5].

3. Input: [5, 12, 11, -1, 12], K = 3
   Output: 11
   Explanation: The 3rd smallest number is '11', as the first two small numbers are [5, -1].

Constraints:
- The array may contain duplicates.
- For the scope of this problem, assume that K is always valid, i.e., 1 ≤ k ≤ array's length.

Tags:
- Array
- Heap
"""

from typing import List

def find_Kth_smallest(nums: List[int], k: int) -> int:
    return -1