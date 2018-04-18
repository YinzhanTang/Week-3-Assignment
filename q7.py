# Q7: How common is the most common first name? Which is it?
import helper # Import Module 'helper'

data = helper.read_salaries() #Parse 'salaries.csv' and return a nested list
names = helper.get_column(data, 1) # Get first names column
counts = helper.counts(names) # Count first names

print(helper.dict_max_value(counts)) # Print maximum
print(helper.dict_max_value(counts)[0] + ' is the most common first name.'
    +'There are',helper.dict_max_value(counts)[1],'employees who have this name.')

# MICHAELJ is the most common first name.There are 268 employees who have this name.
