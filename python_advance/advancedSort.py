#Merge Sort:Divide and conquer
def merge_sort(arr):
    if len(arr) > 1:
        # Find the middle point
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursive sorting of both halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge sorted halves
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Check if any elements are left
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

# Example usage
numbers = [38, 27, 43, 3, 9, 82, 10]
sorted_numbers = merge_sort(numbers)
print("Sorted array using Merge Sort:", sorted_numbers)


#Quick Sort is also a divide-and-conquer algorithm
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

# Example usage
numbers = [10, 7, 8, 9, 1, 5]
sorted_numbers = quick_sort(numbers)
print("Sorted array using Quick Sort:", sorted_numbers)

#Heap Sort involves building a binary heap structure from the array. 
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Check if left child exists and is greater than root
    if left < n and arr[largest] < arr[left]:
        largest = left

    # Check if right child exists and is greater than root
    if right < n and arr[largest] < arr[right]:
        largest = right

    # Swap and continue heapifying if root is not the largest
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Build a maxheap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements from heap
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        heapify(arr, i, 0)
    return arr

# Example usage
numbers = [12, 11, 13, 5, 6, 7]
sorted_numbers = heap_sort(numbers)
print("Sorted array using Heap Sort:", sorted_numbers)
