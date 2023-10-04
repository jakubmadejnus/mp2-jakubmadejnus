"""
Problem: Find the Next Letter

Description:
Given an array of lowercase letters sorted in ascending order, determine the smallest letter in the given array greater than a specified 'key'. Assume the array is a circular list, which means that the last letter is assumed to be connected with the first letter. This implies that the smallest letter in the array is greater than the last letter of the array and is also the first letter of the array. Write a function to return the next letter of the given 'key'.

Function Signature:
def find_next_letter(letters: List[str], key: str) -> str:

Inputs:
    - letters (List[str]): A list of lowercase letters sorted in ascending order. 
    - key (str): A single lowercase letter for which we need to find the next letter in the array.

Returns:
    - str: The next letter of the specified 'key' from the given list.

Examples:
1. Input:
        letters = ['a', 'c', 'f', 'h'], key = 'f'
   Output: 'h'
   Explanation: The smallest letter greater than 'f' is 'h' in the given array.

2. Input:
        letters = ['a', 'c', 'f', 'h'], key = 'b'
   Output: 'c'
   Explanation: The smallest letter greater than 'b' is 'c'.

3. Input:
        letters = ['a', 'c', 'f', 'h'], key = 'm'
   Output: 'a'
   Explanation: As the array is assumed to be circular, the smallest letter greater than 'm' is 'a'.

4. Input:
        letters = ['a', 'c', 'f', 'h'], key = 'h'
   Output: 'a'
   Explanation: As the array is assumed to be circular, the smallest letter greater than 'h' is 'a'.

Notes:
    - Binary Search can be utilized to solve the problem efficiently due to the sorted nature of the list.

Tags:
    - Binary Search
    - Arrays
"""
from typing import List

def find_next_letter(letters: List[str], key: str) -> str:
  return ""