import heapq

data = [10, 20 ,43, 1, 2, 65, 17, 44, 2, 3, 1]
heapq.heapify(data)

# print(data)
# print(heapq.heappop(data))
# print(data.pop())
# print(data)

# Heap Insertion

heapq.heappush(data, 4)
print(data)

# To use the MaxHeap, negate all the values in data and heapify
data_max = [-x for x in data]
heapq.heapify(data_max)
print(data_max)

# Using undocumented functions
heapq._heapify_max(data)
print(data)

print(heapq._heappop_max(data))
print(data)


# Merging two lists with sorted order
l1 = [10, 20, 30, 40, 50]
l2 = [15, 25, 35, 45, 55]

l3 = heapq.merge(l1, l2)
print(list(l3))
