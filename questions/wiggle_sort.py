"""
Problem: Wiggle Sort

Description:
Given an integer array "nums", reorder its elements in such a way that nums[0] <= nums[1] >= nums[2] <= nums[3].... You can assume that the given input will always have a valid answer.

Function Signature:
def wiggleSort(nums: List[int]) -> List[int]:

Inputs:
    - nums (List[int]): An array of integers where 1 <= nums.length <= 5 * 104 and 0 <= nums[i] <= 104.

Returns:
    - List[int]: The array after performing wiggle sort on it.

Examples:

1. Input:
        nums = [3,5,2,1,6,4]
   Output: [3,5,1,6,2,4]
   Explanation: [1,6,2,5,3,4] is also a valid wiggle sorted array.

2. Input:
        nums = [6,6,5,6,3,8]
   Output: [6,6,5,6,3,8]
   Explanation: The given input already satisfies the wiggle sort condition.

Notes:
    - One can first sort the array and then perform the reordering.
    - Another approach is to iterate over the array and swap adjacent elements if they don't satisfy the wiggle condition. This approach can achieve the solution in O(n) time complexity.

Follow-up: 
    - Can you solve the problem in O(n) time complexity?

Tags:
    - Arrays
    - Sorting
    - Two Pointers
"""

from typing import List

def wiggleSort(nums: List[int]) -> List[int]:

    n = len(nums) - 1

    for i in range(n):
        if (i % 2 == 0):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
        else:
            if nums[i] < nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
 
    return nums