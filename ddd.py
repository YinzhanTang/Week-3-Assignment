
def read_salaries(): # Define a new function called 'read_salaries'
    file = open('salaries.csv') # Open the 'salaries.csv'
    salaries = [] # Define a new list called 'salaries'
    for line in file: # Iteration startup
        if 'Name' not in line: # Ignore the first (header) line in the iteration
            fields = line[:-1].split(',') # Break up every line into fields. Split each line on ','
            fields[0] = fields[0].replace('"','') # Update the parsing by removing quotation marks.

            fields[1] = fields[1].replace('"','').replace(' ','') # Removing quotation marks and extra white space
            fields[7] = fields[7].replace('$','') # Removing the dollar sign
            salaries.append(fields)# Add all these list of fields in the list 'salaries'
    return salaries # Determine the return value of the function
    print(salaries) # Print the list 'salaries'
