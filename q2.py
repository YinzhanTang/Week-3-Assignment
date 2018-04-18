# Q2: How many full time employees are there?
import helper # Import Module 'helper'
data = helper.read_salaries() # Parse 'salaries.csv' and return a nested list
column = helper.get_column(data, 4) # Get the column 'Full or Part-Time'
Number = helper.count(column, 'F') # Count the number of full time employees
print('There are', Number, 'full time employees.') # Print the answer

# There are 31090 full time employees.
