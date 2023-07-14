def heapify(arr,i,n):
    largest = i
    left_child = 2*i + 1
    right_child = 2*i + 2

    # if the left child is larger
    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child
    # if the right child is larger
    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child

    # if largest is no longer the root element, swap it and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr,largest,n)

def heap_sort(arr):
    n = len(arr)
    # we need to start from the bottom subtree up to the root node, aka from n//2 - 1 till we reach 0
    # the goal is to make a binary tree where each subtree's root is the largest number
    for i in range(n//2 - 1,-1,-1):
        heapify(arr,i,n)

    # after the max heap is constructed, we actually sort 
    for i in range(n-1,0,-1):
        arr[i],arr[0] = arr[0],arr[i] # this swap ensures that the largest element goes from the root to end of the arr, so we know it is sorted

        heapify(arr,0,i) #make sure the new root is again the largest

a = [1,4,6,2,3,9,8,10,20,3,4]
heap_sort(a)

print("Sorted: ",a)