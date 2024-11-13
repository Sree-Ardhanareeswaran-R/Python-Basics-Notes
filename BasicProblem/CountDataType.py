# Function to count the number of data type in a list
def count_data_type(array):
    count = {}

    for ele in array:
        ele_type = type(ele)
        # If element is there it get the value of element add 1 otherwise it take default element and add 1
        count[ele_type] = count.get(ele_type, 0) + 1

    return count

data_list = [1, 'hello', 3.14, True, 2, 'world', False, 3.14]
print(count_data_type(data_list))