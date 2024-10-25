#Insertion Sort

def insertion_sort(arr):
    for i in range(1, len(arr)):
        # Store the current element
        key = arr[i]
        j = i - 1
        # Move elements of arr[0...i-1] that are greater than key to one position ahead
        # of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        # Place key in its correct position
        arr[j + 1] = key
    return arr

# Example usage
numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = insertion_sort(numbers)
print("Sorted array:", sorted_numbers)
