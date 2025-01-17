# Class Node has constructor __init__ which initializes the newly create object of that class
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

# Class LinkedList is used to define methods for creating and manipulating linkedlist
class LinkedList:
    def __init__(self):
        self.head = None

    # Method for inserting data value at the beginning of LinkedList
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
    
    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return
        itr = self.head
        llstr = ''
        
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next

        print(llstr)

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(89)
    ll.print()