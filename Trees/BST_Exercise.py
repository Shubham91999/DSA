class BinarySearchTree:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if self.data == data:
            return
        
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
        else:
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
    
    def pre_order_traversal(self):
        elements = []

        # Visit base node
        elements.append(self.data)
        # Visit left node
        if self.left:
            elements += self.left.pre_order_traversal()
        # Visit right node
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements
    
    def post_order_traversal(self):
        elements = []

        # Visit left node
        if self.left:
            elements += self.left.post_order_traversal()
        # Visit right node
        if self.right:
            elements += self.right.post_order_traversal()
        # Visit base node
        elements.append(self.data)

        return elements
    
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
    
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()
    
    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        # Do not forget to add current data to left & right subtree's sum
        return self.data + left_sum + right_sum



# Class BinarySearchTree End



def build_tree(elements):
    root = BinarySearchTree(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])
    
    return root

if __name__ == '__main__':
    numbers = [34, 54, 2, 66, 78, 12, 32, 28, 24, 90, 11]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.pre_order_traversal())
    print(numbers_tree.post_order_traversal())

    print("Minimum Element: ", numbers_tree.find_min())
    print("Maximum Element: ", numbers_tree.find_max())
    print("Sum of all elemtns: ", numbers_tree.calculate_sum())




    