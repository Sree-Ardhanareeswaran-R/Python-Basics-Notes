def sort(lst):
    if len(lst) <= 1:
        return lst


def merge(arr1, arr2, arr3):
    i, j, k = 0, 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr3[k] = arr1[i]
            i += 1

        else:
            arr2[k] = arr2[j]
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