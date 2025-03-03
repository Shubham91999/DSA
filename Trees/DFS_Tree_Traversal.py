class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Preorder Traversal (Root → Left → Right)
def preorder_traversal(root):
    if root:
        print(root.value, end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)

# Inorder Traversal (Left → Root → Right)
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end=" ")
        inorder_traversal(root.right)

# Postorder Traversal (Left → Right → Root)
def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.value, end=" ")

# Example Usage:
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    #     1
    #    / \
    #   2   3
    #  / \
    # 4   5


    print("Preorder Traversal:")
    preorder_traversal(root)  # Output: 1 2 4 5 3

    print("\nInorder Traversal:")
    inorder_traversal(root)  # Output: 4 2 5 1 3

    print("\nPostorder Traversal:")
    postorder_traversal(root)  # Output: 4 5 2 3 1
