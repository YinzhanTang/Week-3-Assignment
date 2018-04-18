import helper # Import Module 'helper'
data = helper.read_salaries()
salaries = []
for value in helper.get_column(data, 7):
    value = int(value)
    salaries.append(value)
