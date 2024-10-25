#Bubble Sort
#Example-1
def bubbleSort(list):
  n = len(list)
  for i in range(n):
    for j in range(n-1):
      if list[j] > list[j+1] :
        temp = list[j]
        list[j] = list[j+1]
        list[j+1] = temp
  return list

#now test it
nums = [64, 34, 25, 12, 22, 11, 90]
sorted_nums = bubbleSort(nums)
print(sorted_nums)

#Example-2
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Track if any swaps are made
        swapped = False
        for j in range(0, n-i-1):
            # Compare adjacent elements
            if arr[j] > arr[j+1]:
                # Swap if the element is greater than the next element
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # If no swaps are made, the list is already sorted
        if not swapped:
            break
    return arr

# Example usage
numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = bubble_sort(numbers)
print("Sorted array:", sorted_numbers)
