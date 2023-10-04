"""
Problem: Red-Black Tree Implementation

Description:
A Red-Black Tree is a self-balancing binary search tree where each node has an extra bit for denoting the color of the node, either red or black. Red-Black Tree satisfies the following properties:
1. Every node is either red or black.
2. The root is black.
3. All leaves are black.
4. If a red node has children then, the children are always black.
5. Every simple path from a node to any of its descendant leaves has the same black height (number of black nodes).

Please implement the following methods for the Red-Black Tree:
1. insert: Inserts a node into the Red-Black tree and ensures tree remains balanced.
You need to make sure that the insert method correctly maintains the Red-Black Tree properties. 
3. leftRotate: Performs left rotation on the tree.
4. rightRotate: Performs right rotation on the tree.

The Red-Black Tree should be maintained after every insert and delete operation.

Function Signature:
class RBNode:
    def __init__(self, key, color, parent=None, left=None, right=None):
        self.key = key
        self.color = color
        self.parent = parent
        self.left = left
        self.right = right

class RBTree:
    ... you may modify the class definition here ...

    def __init__(self, root=None):
        self.root = root

    def leftRotate(self, x: RBNode) -> None:
        pass
    
    def rightRotate(self, y: RBNode) -> None:
        pass

Examples:
1. RBTree should rotate left when right child is red after an insert operation.
2. RBTree should balance itself by doing a right rotation when the left child is red after an insert operation.

Tags:
    - Red-Black Tree
    - Binary Search Tree
    - Trees
    - Rotation
    - Self-balancing
"""

class RBNode:
    RED = 0
    BLACK = 1
    
    def __init__(self, key, color=RED, parent=None, left=None, right=None):
        self.key = key
        self.color = color
        self.parent = parent
        self.left = left
        self.right = right

class RBTree:
    def __init__(self):
        self.NIL_LEAF = RBNode(None, RBNode.BLACK)  # Changed this line
        self.root = self.NIL_LEAF

    def insert(self, key) -> None:
        # TODO: Implement insert method and ensure tree remains balanced
        return None
    
    def leftRotate(self, x: RBNode) -> None:
        # TODO: Implement leftRotate method
        return None
    
    def rightRotate(self, y: RBNode) -> None:
        # TODO: Implement rightRotate method
        return None
    
    # Helper method to get keys in a sorted order
    def get_sorted_keys(self):
        keys = []

        def inorder_traversal(node):
            if node.key is not None:
                inorder_traversal(node.left)
                keys.append(node.key)
                inorder_traversal(node.right)

        inorder_traversal(self.root)
        return keys