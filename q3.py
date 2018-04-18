# Q3: How many part-time employees are there?
import helper # Import Module 'helper'
data = helper.read_salaries() # Parse 'salaries.csv' and return a nested list
column = helper.get_column(data, 4) # Get the column 'Full or Part-Time'
Number = helper.count(column, 'P') # Count the number of part time employees
print('There are', Number, 'full time employees.') # Print the answer

# There are 2093 part time employees.
