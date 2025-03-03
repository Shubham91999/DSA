# Class to create new Tree Nodes
class TreeNode:

    # Constructor
    def __init__(self, data):
        # To store value
        self.data = data
        # List will contain instances of TreeNode class
        self.children = []
        self.parent = None

    # Function to add child node 
    def add_child(self, child):
        # Setting parent as current node will be parent of new child node
        child.parent = self
        # Adding new child node in list of current node's children list
        self.children.append(child)

    # Function to get level of particular node by counting no of parents
    def get_level(self):
        # Variable to store level
        level = 0

        p = self.parent
        # Iterate till the current node has parent node
        while p:
            # Incrementing level counter
            level += 1
            # Assigning parent node to current node to traverse in reverse
            p = p.parent
        return level
        


    def print_tree(self):
        # Based on level defining spaces 
        spaces = ' ' * self.get_level() * 3
        # Checking if root node, no spaces attached
        prefix = spaces + '|--' if self.parent else ''
        
        print(prefix + self.data)

        if self.children:
            for child in self.children:
                child.print_tree()


def build_product_tree():
    # Adding root to tree
    root = TreeNode('Electronics')

    # Adding child node Laptop and its child nodes
    laptop = TreeNode('Laptop')
    laptop.add_child(TreeNode('Mac'))
    laptop.add_child(TreeNode('Surface'))
    laptop.add_child(TreeNode('Thinkpad'))

    # Adding child node Cell Phone and its child nodes
    cellphone = TreeNode('Cell Phone')
    cellphone.add_child(TreeNode('iPhone'))
    cellphone.add_child(TreeNode('Google Pixel'))
    cellphone.add_child(TreeNode('Vivo'))

    # Adding child node TV and its child nodes
    tv = TreeNode('TV')
    tv.add_child(TreeNode('Samsung'))
    tv.add_child(TreeNode('LG'))

    # Adding parent nodes to root
    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    #print(tv.get_level())
    return root



if __name__ == '__main__':
    root = build_product_tree()
    root.print_tree()
    #print(root.get_level())
    pass

