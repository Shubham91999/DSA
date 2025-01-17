# Class Node has constructor __init__ which initializes the newly create object of that class
class Node:
    def __init__(self, data=None, next=None):
        self.data = data #Stores the actual data
        self.next = next #Points to the next node in the list

# Class LinkedList is used to define methods for creating and manipulating linkedlist
class LinkedList:
    def __init__(self):
        self.head = None #Initially the linked list is empty, so 'head' is none

    # Method for inserting data value at the beginning of LinkedList
    def insert_at_beginning(self, data):
        # Creating new node class object with data provided in method call 
        # New Node's 'next' points to the current 'head' node
        # Self.head serves an a reference to the first node of the linked list
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