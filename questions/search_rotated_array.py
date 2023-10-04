"""
Problem: Find Element in Rotated Sorted Array

Description:
Given a rotated sorted array without duplicates, find if a given 'key' is present in it.
Return the index of the 'key' in the rotated array. If the 'key' is not present, return -1.

Function Signature:
def search_rotated_array(nums: List[int], key: int) -> int:

Inputs:
    - nums (List[int]): A list of integers which is sorted in ascending order and then rotated.
    - key (int): An integer you want to search for.

Returns:
    - int: The index of the key if it's present, else -1.

Examples:

1. Input:
    nums = [10, 15, 1, 3, 8]
    key = 15
   Output: 1

2. Input:
    nums = [4, 5, 7, 9, 10, -1, 2]
    key = 10
   Output: 4

Notes:
    - A binary search approach can be adapted to handle the rotation in the sorted array.
"""

from typing import List

def search_rotated_array(nums: List[int], key: int) -> int:
    return 0
