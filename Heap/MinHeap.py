class MinHeap:

    def __init__(self, heapSize):
        # Steps to create heap -> 1) Create complete binary tree using an array 2) Use that binary tree to construct a heap
        self.heapSize = heapSize
        # Number of elements needed while instatiating an array
        self.minHeap = [0] * (heapSize+1)
        # Number of nodes in heap
        self.realSize = 0

    # Function to add new element in heap
    def add(self, element):
        self.realSize += 1              # Incrementing current number of nodes in heap
        if self.realSize > self.heapSize: # If heap is already full, print message and return 
            print("Too many elements") 
            self.realSize -= 1
            return
        
        # If space available, add new element
        self.minHeap[self.realSize] = element    # Updated realsize gives us the last empty location, adding in last to preserve completeness of tree
        index = self.realSize   # Stroring its index for further comparisons
        parent = index // 2   # Getting parent location for comparison

        # If newly added element is smaller than its parent, it'll be swapped with the parent
        while self.minHeap[index] < self.minHeap[parent] and index > 1:
            self.minHeap[parent], self.minHeap[index] = self.minHeap[index], self.minHeap[parent]  # Swapping the elements
            index = parent  # Updating index and parent for further checks
            parent = index // 2

    
    # Function to get top element in heap
    def peek(self):
        return self.minHeap[1]
    
    # Function to delete element from heap (Only one element can be popped/deleted at a time) 
    def pop(self):
        # Checking base case, heap is empty
        if self.realSize < 1:
            print("Heap is empty")
            return sys.maxsize
        else:
            # Deleting top element
            removedElement = self.minHeap[1]

            # To maintain completeness of tree, inserting last element at the top position
            self.minHeap[1] = self.minHeap[self.realSize]
            self.realSize -= 1   # Decrementing size of heap

            # Compare top/first element with its child nodes and swap to maintain heap properties
            index = 1
            while (index <= self.realSize // 2):
                left = index * 2   # For accessing left child of current node
                right = (index * 2) + 1 # For accessing right child of current node
                
                if (self.minHeap[index] > self.minHeap[left] or self.minHeap[index] > self.minHeap[right]):
                    if self.minHeap[left] < self.minHeap[right]: # if left child is lesser than right, swap current/index with left
                        self.minHeap[left], self.minHeap[index] = self.minHeap[index], self.minHeap[left]
                        index = left  # updating index as we swapped with left
                    else:
                        self.minHeap[right], self.minHeap[index] = self.minHeap[index], self.minHeap[right]
                        index = right
                else:
                    break
            return removedElement    
        
    # return the number of elements in the Heap
    def size(self):
        return self.realSize

    # Function to print the heap nodes
    def printheap(self):
        print(self.minHeap[1:self.realSize + 1])


if __name__ == "__main__":
    heap = MinHeap(5)
    heap.add(3)
    heap.add(4)
    heap.add(2)
    heap.add(6)
    heap.add(1)
    heap.printheap()
    print(heap.peek())
    print(heap.pop())