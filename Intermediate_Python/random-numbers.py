# ------------------------  Exercise 1
print('\n* Exercise 1*\n')
# Import numpy as np
import numpy as np

# Set the seed
np.random.seed(123)

# Generate and print random float
print(np.random.rand())

# ------------------------  Exercise 2
print('\n* Exercise 2*\n')

# Import numpy and set seed
import numpy as np

np.random.seed(123)

# Use randint() to simulate a dice
print(np.random.randint(1, 7))

# Use randint() again
print(np.random.randint(1, 7))

# ------------------------  Exercise 3
print('\n* Exercise 3*\n')

# Numpy is imported, seed is set

# Starting step
step = 50

# Roll the dice
dice = np.random.randint(1, 7)

# Finish the control construct
if dice <= 2:
    step = step - 1
elif 3 <= dice <= 5:
    step = step + 1
else:
    step = step + np.random.randint(1, 7)

# Print out dice and step
print(dice, step)
