def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Last i elements are already sorted, so we don't need to compare them
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print(f'Swapped {arr[j]} with {arr[j+1]}')

# The list to be sorted
arr = [17, 0, 2, 11, 12, 12, 10, 9]
print("Unsorted array:", arr)
bubble_sort(arr)
print("Sorted array:", arr)
