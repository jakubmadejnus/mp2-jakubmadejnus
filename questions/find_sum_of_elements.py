"""
Problem: Find the Sum of Numbers between the K1th and K2th Smallest Elements

Description:
Given an array of numbers, find the sum of all numbers between the K1’th and K2’th smallest elements of that array.

Function Signature:
def find_sum_between_elements(nums: List[int], k1: int, k2: int) -> int:

Examples:
1. Input: [1, 3, 12, 5, 15, 11], and K1=3, K2=6
   Output: 23
   Explanation: The 3rd smallest number is 5 and 6th smallest number 15. The sum of numbers coming
   between 5 and 15 is 23 (11+12).
   
2. Input: [3, 5, 8, 7], and K1=1, K2=4
   Output: 12
   Explanation: The sum of the numbers between the 1st smallest number (3) and the 4th smallest 
   number (8) is 12 (5+7).

Constraints:
- For the scope of this problem, assume that K1 and K2 are always valid.

Tags:
- Array
- Heap
"""

from typing import List
import heapq

def find_sum_between_elements(nums: List[int], k1: int, k2: int) -> int:
    
   k_smallest_numbers = heapq.nsmallest(k2, set(nums))

   if len(k_smallest_numbers) >= k2:
        k1_val, k2_val = k_smallest_numbers[k1 - 1], k_smallest_numbers[k2 - 1]
   else:
        return 0
   
   sum_between = sum(num for num in nums if k1_val < num < k2_val)

   return sum_between
