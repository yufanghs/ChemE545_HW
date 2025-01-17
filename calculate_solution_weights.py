def calculate_solution_weights(molecular_weights, solutions_needed):

    # Step 1: rearrange the solutions_needed list into column1 = molecule name, column 2 = molecular_weights
    ### Delete the last character "M"
    solution_rearrange = [item[:-1] for item in solutions_needed]
    ### split the terms by "-"
    solution_rearrange = [item.split("-") for item in solution_rearrange]

    
    # Step 2: calculate total weight
    ### Create a empty list (and add output items later)
    output_list = []
    ### Check every items in the list
    for i in range(len(solution_rearrange)):
        ### Check if the name in the "molecular_weights" dict or not
        
        ### if yes, calculate the total weight and append the result into output_list with specified format
        if solution_rearrange[i][0] in molecular_weights.keys():
            amount = float(solution_rearrange[i][1])
            unit_weight = molecular_weights[solution_rearrange[i][0]]
            total_weight = unit_weight * amount
            output_list.append(solution_rearrange[i][0] + "-" + solution_rearrange[i][1] + "M-" + f"{total_weight:.2f}" + "g")
        
        ### if no, append "unknown"
        else:
            output_list.append("unknown")


    return output_list
