# ChemE545_HW0

## extract_parameter(unit_name, parameter_name, index)
  Input (1) unit_name, (2) parameter_name, (3)index
  
  then we can get the result as {unit_name}_{parameter_name}_{value}.
  
  Example: extract_parameter("distillation_column", "temperature", 1) should return "distillation_column_temperature_160".


## calculate_solution_weights(molecular_weights, solutions_needed)
  Input (1) the molecular_weights dictionary, 
  
          for example: molecular_weights = {'NaCl': 58.44, 'H2SO4': 98.079, 'NaOH': 40.00, 'KMnO4': 158.034, 'CH3COOH': 60.052}
          
  and (2) the solution needed
  
          for example solutions_needed = ['NaCl-0.5M', 'H2SO4-0.25M', 'NaOH-1M', 'KCl-0.1M', 'CH3COOH-0.3M']

  Then we can get the weight in the format ['NaCl-0.5M-29.22g', 'H2SO4-0.25M-24.52g', 'NaOH-1M-40.00g', 'unknown', 'CH3COOH-0.3M-18.02g']
  
