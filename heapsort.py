# Heapsort implementation

import math

# Returns index of right child
def right(arr, index):
    return math.floor((2 * index) + 2)

# Returns index of left child
def left(arr, index):
    return math.floor((2 * index) + 1)

# Returns index of parent node
def parent(arr, index):
    return math.floor((index - 1) / 2)

def heapify(arr, index):
    parent_node = arr[parent(arr, index)]
    child_node = arr[index]

    print("\nHeapifying at index {}".format(index))
    print("-> Comparing parent ({}) vs child ({})".format(parent_node, child_node))

    # Swap with the parent node if it is less than the child node
    if parent_node < child_node:
        arr[parent(arr, index)], arr[index] = arr[index], arr[parent(arr, index)] # swap
        print("-> Swapped parent and child node")
        print("-> Parent is now {} and child is now {}".format(arr[parent(arr, index)], arr[index]))

# Builds a max heap from given array
def build_maxheap(arr):
    # Traverse array backwards to heapify from bottom up
    for i in range(len(arr)-1, 0, -1):
        heapify(arr, i)

# Takes a max heap and fully sorts
def heapsort(arr):
    sorted = []
    # Sort from bottom up
    for i in range(len(arr)-1, 0, -1):
        # Currently, the biggest value in array is the root, so we append that to our sorted list
        sorted.append(arr[0])
        # Replace root with current index, and reperform max heap construction in order for root
        # to once again be the largest element
        arr[0] = arr[i]
        del arr[i] #
        build_maxheap(arr)
    return sorted[::-1] # returns ascending sorted list

# Driver code to demonstrate use
data = [4, 13, 65, 47, 1, 23, 12, 32, 75, 20, -99, -2012030, 40, 0, 999999999999999, -69, -33, -1]
print("Data before building max heap: {}".format(data))
build_maxheap(data)
print("\nMax Heap: {}".format(data))
sorted_data = heapsort(data)
print("\nSorted Data: {}".format(sorted_data))
