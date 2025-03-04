class BinarySearchTree:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return 
        
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)

        if data > self.data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)

    def in_order_traversal(self):
        elements = []

        # Visit left node
        if self.left:
            elements += self.left.in_order_traversal()

        # Visit base node
        elements.append(self.data)

        # Visit right node
        if self.right:
            elements += self.right.in_order_traversal()

        return elements
    
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
    
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()
    
    # Function to delete node
    def delete(self, val):
        # 1. Check if the value lies in left or right subtree
        if val < self.data:
            # If it is in left subtree and left present
            if self.left:
                # Recursive call to delete function in left
                self.left = self.left.delete(val)

        elif val > self.data:
            # If found in right subtree
            if self.right:
                # Recursive call to delete in right
                self.right = self.right.delete(val)
        else:
            # Val is not greater and lesser than current node data, it means we found the required node
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right
            
            # Rebalancing the tree
            
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self


        # 2. 





    

    
# End BinarySearchTree class
    
def build_tree(elements):
    root = BinarySearchTree(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    numbers = [17, 4, 1, 21, 9, 23, 18, 16]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.delete(18))
    print(numbers_tree.in_order_traversal())




    