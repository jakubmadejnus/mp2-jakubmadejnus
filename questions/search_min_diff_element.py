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

    if not nums:
        return -1  # or raise an error

    low, high = 0, len(nums) - 1

    # If the key is outside the range of list values,
    # the answer is either the first or last element
    if key < nums[low]:
        return nums[low]
    if key > nums[high]:
        return nums[high]

    # Binary search
    while low <= high:
        mid = low + (high - low) // 2

        # If we find the exact number, it is obviously the minimum difference
        if nums[mid] == key:
            return nums[mid]

        # If the current element is less than the key, move to the right in the array.
        if nums[mid] < key:
            low = mid + 1
        else:
            high = mid - 1  # If it is larger, move to the left

    # At the end of the loop, 'low' is the index of the smallest larger element
    # because we are moving 'mid + 1' and 'mid' to the left side.
    # 'high' is the index of the largest smaller element since we move 'mid - 1'
    # during the search. We then compare these two elements to find the minimum difference.

    # Check which one is closer, we shouldn't have a scenario where low and high are out of range of the array
    if (nums[low] - key) < (key - nums[high]):
        return nums[low]
    else:
        return nums[high]
