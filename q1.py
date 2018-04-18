# Q1: How many employees does the city have?
import helper # Import Module 'helper'
data = helper.read_salaries() # Parse 'salaries.csv' and return a nested list
Number = len(data) # The number of employees is equal to the length of the list
print('The city has', Number , 'employees.') # Print the answer

# The city has 33183 employees.
