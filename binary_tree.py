"""
This module creates a binary tree by passing in a list. This module also prints the tree by row-level, preorder, inorder, and postorder traversal.
"""


class TreeNode:
    """
    This class defines the TreeNode
    """

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def binary_tree_builder(values):
    """
    Method to build the binary tree by passing a list. This builds a row-order tree sequentially
    """

    root = TreeNode(values[0])
    queue = [root]
    index = 1

    while index < len(values):
        current = queue.pop(0)

        if index < len(values):
            current.left = TreeNode(values[index])
            queue.append(current.left)
            index += 1

        if index < len(values):
            current.right = TreeNode(values[index])
            queue.append(current.right)
            index += 1

    return root


def print_row_order(root):
    """
    This will print the values of the nodes in row order.
    """

    queue = []
    output = []
    queue.append(root)

    while queue:
        pop_value = queue.pop(0)
        if pop_value is None:
            continue
        output.append(pop_value.val)
        queue.append(pop_value.left)
        queue.append(pop_value.right)

    print(output)
    return None


def print_preorder(root):
    """
    print preorder traversal
    """

    output = []

    def preorder(root):
        if root is None:
            return None

        output.append(root.val)
        preorder(root.left)
        preorder(root.right)

    preorder(root)
    print(output)
    return None


def print_inorder(root):
    """
    print inorder traversal
    """

    output = []

    def inorder(root):
        if root is None:
            return None

        inorder(root.left)
        output.append(root.val)
        inorder(root.right)

    inorder(root)
    print(output)
    return None


def print_postorder(root):
    """
    print postorder traversal
    """

    output = []

    def postorder(root):
        if root is None:
            return None

        postorder(root.left)
        postorder(root.right)
        output.append(root.val)

    postorder(root)
    print(output)
    return None


arr = [1, 2, 3, 4, 5, 6]
bt = binary_tree_builder(arr)
print_row_order(bt)
print_preorder(bt)
print_inorder(bt)
print_postorder(bt)
