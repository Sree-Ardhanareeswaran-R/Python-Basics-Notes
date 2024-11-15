def selection_sort(arr):
    for i in range(len(arr)):
        low = i
        for j in range(i + 1, len(arr)):
            if arr[low] > arr[j]:
                low = j

        arr[low], arr[i] = arr[i], arr[low]


lst = [64, 25, 12, 22, 11]
selection_sort(lst)
print(lst)
# Output: [11, 12, 22, 25, 64]