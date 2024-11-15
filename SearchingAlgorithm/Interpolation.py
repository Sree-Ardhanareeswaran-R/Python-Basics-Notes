def interpolation_search(lst, tar):
    low, high = 0, len(lst) - 1
    while low <= high and lst[low] < tar < lst[high]:
        mid = low + int(((high - low) / (lst[high] - lst[low])) * (tar - lst[low]))
        
        if lst[mid] == tar:
            return mid
        
        if lst[mid] < tar:
            low = mid + 1
        
        else:
            high = mid - 1
    
    return -1

arr = [10, 20, 30, 40, 50]
target = 30
print(interpolation_search(arr, target))  # Output: 2

arr = [5, 7, 9, 10]
target = 6
print(interpolation_search(arr, target))  # Output: -1