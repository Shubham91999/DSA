class maxHeap:
    def __init__(self, heapSize):
        self.heapSize = heapSize
        self.maxHeap = [0] * (self.heapSize+1)
        self.realSize = 0

    def add(self, element):
        self.realSize += 1
        if self.realSize > self.heapSize:
            print("Too many element")
            self.realSize -= 1
            return
        else:
            self.maxHeap[self.realSize] = element # Added to last in oreder to maintain completeness
            index = self.realSize
            parent = index // 2   # Accessing parent for comparing with new value/ index

            while (self.maxHeap[index] < self.maxHeap[parent] and index > 1):
                self.maxHeap[index], self.maxHeap[parent] = self.maxHeap[parent], self.maxHeap[index]
                index = parent
                parent = index // 2

    def pop(self):
        if self.realSize < 1:
            print("Heap is empty")
            return -sys.maxsize
        else:
            removedElement = self.maxHeap[1]
            self.maxHeap[1] = self.maxHeap[self.realSize]
            self.realSize -= 1
            index = 1

            while (index <= self.realSize // 2):
                left = index * 2
                right = (index * 2) + 1

                if self.maxHeap[index] < self.maxHeap[left] or self.maxHeap[index] < self.maxHeap[right]:
                    if self.maxHeap[left] > self.maxHeap[right]:
                        self.maxHeap[left], self.maxHeap[index] = self.maxHeap[index], self.maxHeap[left]
                        index = left
                    else:
                        self.maxHeap[right], self.maxHeap[index] = self.maxHeap[index], self.maxHeap[right]
                        index = right
                else:
                    break
            return removedElement


    def peek(self):
        return self.maxHeap[1]

    def printheap(self):
        print(self.maxHeap[1:self.realSize+1])


if __name__ == "__main__":
    heap = maxHeap(5)
    heap.add(4)
    heap.add(2)
    heap.add(3)
    heap.printheap()
    heap.pop()
    heap.printheap()