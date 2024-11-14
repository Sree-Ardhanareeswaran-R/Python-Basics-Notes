def convert_elements(input_array, target):
    # Creating dictionary to target the required data type
    target_mapping = {"int" : int, "float" : float, "str" : str}

    # If the target data type is not in dictionary raise a error
    if target not in target_mapping:
        raise ValueError("Unsupported Data Type")

    target = target_mapping[target]
    res = []
    for ele in input_array:
        try:
            # If the risky statement matches the datatype value will be added otherwise exception will be executed
            res.append(target(ele))

        except ValueError:
            continue

    # Result will be returned and the return type is list.
    return res


input_list = ["1", "2", "3.5", "abc", "4"]
target_type = "int"
print(convert_elements(input_list, target_type))