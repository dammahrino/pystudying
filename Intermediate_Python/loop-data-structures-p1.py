# ------------------------  Exercise 1
print('\n* Exercise 1*\n')
# Definition of dictionary
europe = {'spain': 'madrid', 'france': 'paris', 'germany': 'berlin',
          'norway': 'oslo', 'italy': 'rome', 'poland': 'warsaw', 'austria': 'vienna'}

# Iterate over europe
for k, v in europe.items():
    print('the capital of ' + k + ' is ' + v)

# ------------------------  Exercise 1
print('\n* Exercise 2*\n')
# Import numpy as np
import numpy as np

np_height = np.array([74, 74, 72, 75, 75, 73])
np_baseball = np.array([[74, 180], [74, 215], [72, 210]])

# For loop over np_height
for height in np_height:
    print(str(height) + ' inches')

# For loop over np_baseball
for baseball in np.nditer(np_baseball):
    print(baseball)
