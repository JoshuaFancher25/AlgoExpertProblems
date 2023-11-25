# count the number of "1" bits in a binary string
# bit - binary digit
# bit - the smallest unit of information in a computer
# bit - 1 or 0
# byte - 8 bits is one byte

x = 3
sum = 0
while x > 0:
    sum += 1
    x = x & x-1
    # using and bitwise operations with x and x-1 to effectively cancel out the least significant bit

print(sum)