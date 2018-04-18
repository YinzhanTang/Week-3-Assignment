# Q4: How many employees in the police department?
import helper # Import Module 'helper'
data = helper.read_salaries() # Parse 'salaries.csv' and return a nested list
column = helper.get_column(data, 3) # Get the column 'Department'
Number = helper.count(column, 'POLICE') # Count the number employees in the police department
print('There are', Number, 'employees in the police department.') # Print the answer

# There are 13414 employees in the police department.
