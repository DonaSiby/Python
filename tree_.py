class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def mirror_tree(root):
    if root is None:
        return

    # Swap the left and right subtrees
    root.left, root.right = root.right, root.left

    # Recursively mirror the left and right subtrees
    mirror_tree(root.left)
    mirror_tree(root.right)

def print_tree(root, level=0, prefix="Root: "):
    if root is not None:
        print("  " * level + prefix + str(root.val))
        if root.left is not None or root.right is not None:
            print_tree(root.left, level + 1, "L--- ")
            print_tree(root.right, level + 1, "R--- ")

def inOrder(node):      
  if (node == None):
    return
  inOrder(node.left)   
  print(node.data, end=" ")
  inOrder(node.right)

# Example usage:
# Create a sample tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)


inOrder(root)

mirror_tree(root)

inOrder(root)
# The tree is now mirrored

