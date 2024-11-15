def quick_sort(lst, low, high):
    if low >= high:
        return

    pivot = lst[(high + low) // 2]

    start, end = low, high
    while low <= high:
        while lst[low] < pivot:
            low += 1

        while lst[high] > pivot:
            high -= 1

        if low <= high:
            lst[low], lst[high] = lst[high], lst[low]
            low += 1
            high -= 1

    quick_sort(lst, start, high)
    quick_sort(lst, low, end)

arr = [10, 7, 8, 9, 1, 5]
quick_sort(arr, 0, len(arr) - 1)
print(arr)
# Output: [1, 5, 7, 8, 9, 10]

# Example: Repeated elements
arr = [3, 3, 3, 3]
quick_sort(arr, 0, len(arr) - 1)
print(arr)  # Output: [3, 3, 3, 3]

# Example: Already sorted list
arr = [1, 2, 3, 4, 5]
quick_sort(arr, 0, len(arr) - 1)
print(arr)  # Output: [1, 2, 3, 4, 5]

# Example: Reversed list
arr = [5, 4, 3, 2, 1]
quick_sort(arr, 0, len(arr) - 1)
print(arr)  # Output: [1, 2, 3, 4, 5]

# Example: Negative numbers
arr = [0, -1, -3, -2, 1]
quick_sort(arr, 0, len(arr) - 1)
print(arr)  # Output: [-3, -2, -1, 0, 1]
