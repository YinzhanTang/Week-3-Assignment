# Q8: What are the minimum, mean, median, and maximum salaries?
import helper
data = helper.read_salaries()
salaries = []
for value in helper.get_column(data, 7): # Get the column 'Salaries'
    if value != '':
        value = float(value)
        salaries.append(value)
# TODO: get non-empty salaries from data
print('Minimum:', min(salaries))
print('Mean:', helper.mean(salaries))
print('Median:', helper.median(salaries))
print('Maximum:', max(salaries))

# Minimum: 7200.0
# Mean: 86786.99979015153
# Median: 90024.0
# Maximum: 300000.0
