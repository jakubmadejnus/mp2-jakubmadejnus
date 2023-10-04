"""
Problem: Binary Tree Upside Down

Description:
Given the root of a binary tree, turn the tree upside down and return the new root. This upside-down transformation is achieved using the following steps:

The original left child becomes the new root.
The original root becomes the new right child.
The original right child becomes the new left child.
It is guaranteed that every right node has a sibling (a left node with the same parent) and has no children.

Function Signature:

python
Copy code
def upside_down_binary_tree(root: TreeNode) -> TreeNode:
Inputs:

root (TreeNode): The root node of the binary tree. The TreeNode is defined as:
python
Copy code
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
Returns:

TreeNode: The root of the new upside-down binary tree.
Examples:

Input:

python
Copy code
Tree Structure:
     1
   /   \
  2     3
 / \
4   5
Output:

python
Copy code
Tree Structure:
     4
    / \
   5   2
      / \
     3   1
Input:

python
Copy code
Tree Structure:
[]
Output:

python
Copy code
[]
Input:

python
Copy code
Tree Structure:
   1
Output:

Tree Structure:
    1
Notes:

You can visualize this transformation as rotating the tree on its left-most branch.
A non-recursive solution is preferable as we can leverage the iterative nature of the problem.
Tags:

Trees
Recursion (if opting for a recursive solution)
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def upsideDownBinaryTree(root: TreeNode) -> TreeNode:
    return TreeNode()