def linear_search(lst, tar):
    for i, ele in enumerate(lst):
        if ele == tar:
            return i
    
    return -1

arr = [10, 20, 30, 40, 50]
target = 30
print(linear_search(arr, target))  # Output: 2

arr = [5, 7, 9, 10]
target = 6
print(linear_search(arr, target))  # Output: -1
