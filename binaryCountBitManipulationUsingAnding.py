x = 15
sum = 0
while x > 0:
    sum += 1    # with each iteration the sum is incremented by 1
    x &= x - 1  # clears the right most bit - num to binary then num-1 to binary will always
    print(x)
                # cancel out the right most bit
                # the result with bit manipluation be the number with the right most bit set to 0

print(sum)
print(5&1) # 101 & 1
print(5&3)

# bitwise and operation
# bitwise & of n and n-1
# 1 0
# when and-ing a binary number 1&1 = 1 , 1&0 = 0
# both bits must a 1 for the output output to be a 1
# 101 & 100
#   5 &   4
# **************************
# when you do an and with n and n-1 - it effectively flips the least significant bit
# **************************

# when we do bit maninpulation in python with & operator python will internally work
# with the binary representation of the integers. The bitwise and operation is performed
# bit by bit on the binary representation of the numbers.
# - python handles binary representation of integers efficiently
# - other bit manipulation operators ^ & | ~

# bit manipulation - the individual manipulation of bits in a binary representation of data
# bit manipulation is widely used in computer science
# bit is a binary digit