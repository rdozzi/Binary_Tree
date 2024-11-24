class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def binary_tree_builder(values):

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


def print_binary_tree(root):

    queue = []
    output = []
    queue.append(root)

    while queue:
        popValue = queue.pop(0)
        if popValue == None:
            continue
        output.append(popValue.val)
        queue.append(popValue.left)
        queue.append(popValue.right)

    print(output)
    return None
