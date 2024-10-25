#Selection Sort
# Example
def selection_sort(arr):
 for i in range(len(arr)):
    min_idx = i
    for j in range(i+1, len(arr)):
      if arr[min_idx] > arr[j]:
        min_idx = j
      
    # Swap the current with the min element
    temp = arr[i]
    arr[i] = arr[min_idx]
    arr[min_idx] = temp
 return arr

# now test
nums = [64, 25, 12, 22, 11]
sorted_nums = selection_sort(nums)
print(sorted_nums)

#Example-2
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Assume the minimum is the first element
        min_index = i
        for j in range(i+1, n):
            # Update min_index if the element at j is less than the element at min_index
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first element of the unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Example usage
numbers = [64, 25, 12, 22, 11]
sorted_numbers = selection_sort(numbers)
print("Sorted array:", sorted_numbers)
