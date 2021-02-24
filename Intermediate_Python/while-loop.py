# ------------------------  Exercise 1
print('\n* Exercise 1*\n')
# Initialize offset
offset = 8

# Code the while loop
while offset != 0:
    print("correcting...")
    offset = offset - 1
    print(offset)

# ------------------------  Exercise 2
print('\n* Exercise 2*\n')
# Initialize offset
offset = -6

# Code the while loop
while offset != 0:
    print("correcting...")
    if offset > 0:
        offset = offset - 1
    else:
        offset = offset + 1
    print(offset)
