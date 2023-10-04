"""
Problem: Number of Rotations in Rotated Sorted Array

Description:
Given an array of numbers which is sorted in ascending order and is rotated ‘k’ times around a pivot, find ‘k’. The array does not have any duplicates.

Function Signature:
def count_rotations(arr: List[int]) -> int:

Inputs:
    - arr (List[int]): A list of integers representing the rotated sorted array.

Returns:
    - int: The number of times the array has been rotated.

Examples:
1. Input: [10, 15, 1, 3, 8]
   Output: 2
   Explanation: The array has been rotated 2 times.

2. Input: [4, 5, 7, 9, 10, -1, 2]
   Output: 5
   Explanation: The array has been rotated 5 times.

3. Input: [1, 3, 8, 10]
   Output: 0
   Explanation: The array has not been rotated.

Notes:
    - Binary search can be employed. The main task is to find the pivot, which is the minimum element's index in the array.
    - The pivot index will be equivalent to the number of rotations performed on the array.

Tags:
    - Binary Search
    - Arrays
"""

from typing import List

def count_rotations(arr: List[int]) -> int:
  return -1