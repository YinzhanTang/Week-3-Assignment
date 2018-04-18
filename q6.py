# Q7: How big is the largest department? Which one is it?
import helper # Import Module 'helper'
data = helper.read_salaries() # Parse 'salaries.csv' and return a nested list
departments = helper.get_column(data, 3)  # Get the column 'Departments'
counts = helper.counts(departments) # Count departments
maximum = helper.dict_max_value(counts) # Find the maximum
print(helper.dict_max_value(counts)[0] + ' department is the largest department.'
    +'There are',helper.dict_max_value(counts)[1],'employees in this department.')
# Print the maximum

# POLICE department is the largest department.There are 13414 employees in this department.
