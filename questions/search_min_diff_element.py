"""
Problem: Minimum Difference Element

Description:
Given a sorted array of numbers, find the element in the array that has the minimum difference with the given 'key'.

Function Signature:
def find_min_difference_element(nums: List[int], key: int) -> int:

Inputs:
- nums (List[int]): A list of integers sorted in ascending order.
- key (int): The target integer.

Returns:
- int: The element in the list that has the minimum difference with the given 'key'.

Examples:
1. Input: nums = [4, 6, 10], key = 7
Output: 6

2. Input: nums = [4, 6, 10], key = 4
Output: 4

3. Input: nums = [1, 3, 8, 10, 15], key = 12
Output: 10

4. Input: nums = [4, 6, 10], key = 17
Output: 10

Notes:
- The binary search approach can be used to find the position or nearest position of 'key' in the list.
- After finding the position, compare the differences of neighboring numbers to find the minimum difference.

Tags:
- Arrays
- Binary Search
"""

from typing import List

def find_min_difference_element(nums: List[int], key: int) -> int:
  return -1