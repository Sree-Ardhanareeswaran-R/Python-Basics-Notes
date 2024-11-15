def sort(lst):
    if len(lst) <= 1:
        return lst
    
    left = lst[:len(lst) // 2]
    right = lst[len(lst) // 2 :]

    sort(left)
    sort(right)

    merge(left, right, lst)


def merge(arr1, arr2, arr3):
    i, j, k = 0, 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr3[k] = arr1[i]
            i += 1

        else:
            arr3[k] = arr2[j]
            j += 1

        k += 1

    while i < len(arr1):
        arr3[k] = arr1[i]
        i += 1
        k += 1

    while j < len(arr2):
        arr3[k] = arr2[j]
        j += 1
        k += 1

# Input
arr = [38, 27, 43, 3, 9, 82, 10]
sort(arr)
print(arr)