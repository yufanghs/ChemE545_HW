def extract_parameter(unit_name, parameter_name, index):
    # check if the index input is integer and is within range
    if index in [0, 1, 2]:
        # get the value from the dictionary
        value = str(unit_operations_data[unit_name][parameter_name][index])
        # return the desired output {unit_name}_{parameter_name}_{value}
        return unit_name + "_" + parameter_name + "_" + value
    else:
        # if the index is out of range, return "Invalid input"
        return "Invalid input"
