def bubble_sort(arr):
    for i in range(len(arr) - 1):
        swapped = False
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

lst = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(lst)
print (lst)

# Output: [11, 12, 22, 25, 34, 64, 90]