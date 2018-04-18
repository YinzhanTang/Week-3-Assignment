# Q5: How many detectives?
import helper # Import Module 'helper'
data = helper.read_salaries() # Parse 'salaries.csv' and return a nested list
column = helper.get_column(data, 2) # Get the column 'Job Titles'
dictionary = helper.counts(column) # Get a dictionary of value-count pairs of the 'Job Titles' column
Number = dictionary['POLICE OFFICER (ASSIGNED AS DETECTIVE)']
# The number of detectives is equal to the value of key'POLICE OFFICER (ASSIGNED AS DETECTIVE)''
print('There are', Number, 'detectives.') # Print the answer

# There are 989 detectives.
