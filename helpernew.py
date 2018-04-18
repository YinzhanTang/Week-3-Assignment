# A.1: Parse the included salaries.csv file.
# Your parser should split each line on ',' and return a nested list
# where each element is itself a list of fields.
# Additionally you should ignore/remove the first (header) line.

def read_salaries(): # Define a new function called 'read_salaries'
    file = open('salaries.csv') # Open the 'salaries.csv'
    salaries = [] # Define a new list called 'salaries'
    for line in file: # Iteration startup
        if 'Name' not in line: # Ignore the first (header) line in the iteration
            fields = line[:-1].split(',') # Break up every line into fields
        
            salaries.append([fields[0].replace('"','')]+[fields[1].replace('"','').replace(' ','')]
            + fields[2:6]+[fields[7].replace('$','')] + [fields[8]])
            # Add all these list of fields in the list 'salaries'
    return salaries # Determine the return value of the function
    print(salaries) # Print the list 'salaries'

# A.2: Given a 2d list data and an integer column_index
# return a 1d list of values for that column.
def get_column(data, column_index): # Define a new function called 'get_column'
    column = [] # Define a new list called 'column'
    for row in data: # Iteration startup
        column.append(row[column_index]) # Add the chosen row in the 2d list into the new list
    return column # Determine the return value of the function
    print (column) # Print the list 'column'

# A.3: Given a 1d list of `values` (e.g. the result of get_column),
# return the number of elements that are equal to `search_value`.
def count(values, search_values): # Define a new function called 'count'
    count = 0 # Define new variable 'count' which equals 0 at first
    for element in values: # Iteration startup
        if element == search_values: # Determine if certain element equals 'search_value'
            count += 1 # If equals 'search_value', add 1 to 'count'
    return count # Determine the return value of the function, which is the
                # number of elements that are equal to `search_value`.
    print (count) # Print the outcome

# A.4: Given a 1d list values (e.g. the result of get_column),
# return a dictionary of value-count pairs.
def counts(values): # Define a new function called 'values'
    counts = {} # Define a new dictionary called 'counts' which contains nothing at first
    for element in values: # Iteration startup
        if element not in counts: # Determine if certain element is in the dictionary
            counts[element] = 1 # If not in the dictionary, put it in and counts as one
        else:
            counts[element] += 1 # If in the dictionary,counts one more time
    return counts # Determine the return value of the function，which is a
                # dictionary of value-count pairs.
    print(counts) # Print the return value

# A.5: Given a dictionary d with numeric values, return a list [key, value] of two elements,
# where key is the the key in d with the largest value, and value is it's value.
def dict_max_value(d): # Define a new function called 'dict_max_value'
    for key in d: # Iteration startup
        if d[key] == max(d.values()): # Determine if the key has the largest value
            return [key, d[key]] # If it has, return a list of the key and the largest value
            print (key, d[key]) # Print the resulting list

# A.6: Given a list of numbers use the built-in functions sum and len to return their mean.
def mean(numbers): # Define a new function called 'mean'
    mean = sum(numbers)/len(numbers) # Calculate the mean with given list
    return mean # Return the mean

# A.7: Given a list of numbers calculate the median.
def median(numbers): #  Define a new function called 'median'
    if len(numbers) % 2 == 0: # Determine if the length of the given list is even
        median = sum(sorted(numbers)[int(len(numbers)/2-1):int(len(numbers)/2+1)])/2.0
        # Find the median when the length is even
    else: # If the length is odd
        median = sorted(numbers)[int(len(numbers)/2)]
        # Find the median when the length is odd

    return median # Return the median
