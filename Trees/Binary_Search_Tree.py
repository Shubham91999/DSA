class BinarySearchTree:
    # Constructor
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    # Adding child nodes in BST
    def add_child(self, data):

        # While adding child nodes, first we need to check two conditions: 
        # 1. If it is already present in tree or not (BST can't have duplicate items)
        # 2. Whether it is less than current node or right node

        # Checking first condition
        if data == self.data:
            # If data already present, do not add and return None
            return 
        
        # Checking second condition (less than or greater than)
        # If data is less than current node's data
        if data < self.data:
            # Add data in left subtree
            # If node present in left of current node, call add_child recursively to compare data value and insert accordingly
            if self.left:
                self.left.add_child(data)
            else:
                # If no node in left, simple create new BST object and insert
                self.left = BinarySearchTree(data)


        else:
            # Add data in right subtree
            # If node present in right of current node, call add_child recursively to compare data value and insert accordingly
            if self.right:
                self.right.add_child(data)
            else:
                # If no node in left, simple create new BST object and insert
                self.right = BinarySearchTree(data)

    def in_order_traversal(self):
        elements = []

        # Inorder Traversal: 1. Visit left node -> 2. Visit base node -> 3. Visit right node

        # Visiting left node
        if self.left:
            elements += self.left.in_order_traversal()

        # Visiting base node
        elements.append(self.data)

        # Visiting right node
        if self.right:
            elements += self.right.in_order_traversal()

        return elements
    
    # Function for preorder traversal: 1. Visit base node -> 2. Visit left node -> 3. Visit right node
    def pre_order_traversal(self):
        elements = []

        elements.append(self.data)

        if self.left:
            elements += self.left.pre_order_traversal()
        
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements
    
    # Function for preorder traversal: 1. Visit left node -> 2. Visit right node -> 3. Visit base node
    def post_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.pre_order_traversal()
        
        if self.right:
            elements += self.right.pre_order_traversal()

        elements.append(self.data)
            
        return elements
    
    def search(self, val):
        # While sarching data value in BST: 1. Check with current nodes data 
        # -> 2 . If less than current data, search recursively in left subtree 
        # -> 3. If greater, search recursively in right subtree

        if self.data == val:
            return True
        
        # Data might be in left subtree
        if val < self.data:
            # If left node present
            if self.left:
                return self.left.search(val)
            else:
                return False

        else:

            # If right node present
            if self.right:
                return self.right.search(val)
            else:
                return False
            
    # def find_min(self) -> float:
    #     return min(self.in_order_traversal())
    
    # def find_max(self) -> float:
    #     return max(self.in_order_traversal())

    # Above fuctions take O(n), as we traverse all the nodes in inorder traversal
    # Writing min, max functions with lesser time complexity

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
    
    # Sum calculation can be written in both ways, same time complexity O(n)
    def calculate_sum(self) -> float:
        return sum(self.in_order_traversal())

    # def calculate_sum(self):
    #     left_sum = self.left.calculate_sum() if self.left else 0
    #     right_sum = self.right.calculate_sum() if self.right else 0
    #     return self.data + left_sum + right_sum

    
def build_tree(elements):
    root = BinarySearchTree(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root
    

if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.pre_order_traversal())
    print(numbers_tree.post_order_traversal())

    print(numbers_tree.search(20))
    print(numbers_tree.search(23))
    print(numbers_tree.search(220))

    countries = ['India', 'Pakistan', 'Germany', 'USA', 'China', 'Russia', 'India', 'UK', 'USA']
    countries_tree = build_tree(countries)
    print(countries_tree.in_order_traversal())
    print('Is India in the list ? -> ', countries_tree.search('India'))

    print('Minimum in numbers: ', numbers_tree.find_min())
    print('Maximum in numbers: ', numbers_tree.find_max())
    print('Sum of elements: ', numbers_tree.calculate_sum())