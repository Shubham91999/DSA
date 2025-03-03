# Using Queue Iteratively
from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def breadth_first_traversal(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        result.append(node.val)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return result

# Example usage:
# Creating a sample tree:
#        1
#       / \
#      2   3
#     / \   \
#    4   5   6

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

print(breadth_first_traversal(root))  # Output: [1, 2, 3, 4, 5, 6]


# Using Stack Recursively
class TreeNode:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# Recursive function for level order traversal
def levelOrderRec(root, level, res):
    if not root:
        return

    # Add a new level to the result if needed
    if len(res) <= level:
        res.append([])

    # Add current node's data to its corresponding level
    res[level].append(root.data)

    # Recur for left and right children
    levelOrderRec(root.left, level + 1, res)
    levelOrderRec(root.right, level + 1, res)

# Function to perform level order traversal
def levelOrder(root):
    res = []
    levelOrderRec(root, 0, res)
    return res

# Example Tree:
#        1
#       / \
#      2   3
#     / \   \
#    4   5   6

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

print(levelOrder(root))  
# Output: [[1], [2, 3], [4, 5, 6]]

