# create variable
x = 10

# use bin() function / method to convert a integer to binary
# returns a string of the binary counts
y = bin(x)
print(y)

# to print just the binary portion take a string slice
print(y[2:])

# use the count method to count the 1's
print(y.count("1"))

# mathematical method to convert an integer to binary
def binary_count_ones(num):
    count = 0
    while num != 0:
        count += num % 2
        num = num // 2

    return count
print(binary_count_ones(x))