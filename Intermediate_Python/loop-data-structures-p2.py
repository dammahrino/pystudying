# ------------------------  Exercise 1
print('\n* Exercise 1*\n')
# Import cars data
import pandas as pd

cars = pd.read_csv('cars.csv', index_col=0)

# Iterate over rows of cars
for label, row in cars.iterrows():
    print(label)
    print(row)
    print('\n')

# ------------------------  Exercise 2
print('\n* Exercise 2*\n')

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col=0)

# Adapt for loop
for lab, row in cars.iterrows():
    print(lab + ': ' + str(row['cars_per_cap']))

# ------------------------  Exercise 3
print('\n* Exercise 3*\n')

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Code for loop that adds COUNTRY column
for label, row in cars.iterrows():
    cars.loc[label, 'COUNTRY'] = (row['country']).upper()

# Print cars
print(cars)

# ------------------------  Exercise 4
print('\n* Exercise 4*\n')

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col=0)

# Use .apply(str.upper)
cars['COUNTRY'] = cars['country'].apply(str.upper)

print(cars)
