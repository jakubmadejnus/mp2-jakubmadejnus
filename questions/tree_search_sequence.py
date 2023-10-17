"""
Problem: Verify Preorder Sequence in Binary Search Tree

Description:
Given an array of unique integers 'preorder', return true if it is the correct preorder traversal sequence of a binary search tree.

Function Signature:
def verify_preorder(preorder: List[int]) -> bool:

Inputs:
    - preorder (List[int]): A list of integers representing the preorder traversal of a binary tree.

Returns:
    - bool: True if the given preorder sequence can be the traversal of a binary search tree. False otherwise.

Examples:

1. Input:
        preorder = [5,2,1,3,6]
   Output: True

2. Input:
        preorder = [5,2,6,1,3]
   Output: False

Notes:
    - The stack-based approach can be utilized.
    - Keep track of a lower bound for every number and update it when moving to the right subtree.

Tags:
    - Trees
    - Stack
"""

from typing import List

def verify_preorder(preorder: List[int]) -> bool:
    stack = []
    lower = float('-inf')

    for value in preorder:
        if value < lower:
            return False

        while stack and value > stack[-1]:
            lower = stack.pop()

        stack.append(value)
    return True