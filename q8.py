# Q8: What are the minimum, mean, median, and maximum salaries?
import helper
data = helper.read_salaries()
salaries = []
for value in helper.get_column(data, 7): # Get the column 'Salaries'
    if value != '':
        value = float(value[1:])
        salaries.append(value)
# TODO: get non-empty salaries from data
print('Minimum:', min(salaries))
print('Mean:', helper.mean(salaries))
print('Median:', helper.median(salaries))
print('Maximum:', max(salaries))

#Minimum: 2.65
#Mean: 32.78855771628128
#Median: 35.6
#Maximum: 109.0
