# computing the hamming weight of an integer
# hamming weight of a number of the number of bits with a value of 1 in the number
# hamming weight is used in
# - information theory
# - error detection
# - cryptography
# = used in bit manipulation
# ---- n % 2 - effectively calculates the remainder checking the least significant bit
# ---- if the least significant bit is a 1 then n % 2 == 1
# ---- n // 2 - will effectively shift the bits to the right by one position
# -------- 1010 will become 101 with the previous calculation
# -------- this only works because binary is base 2
# -------- binary is a series of powers of 2
# -------- thus - counting the number of times 2 divides into the number is equivalent
# --------      - counting the set bits in binary representation

n = 10
count = 0
while n > 0:
    count += n % 2
    n //= 2
    print("the current value of n:" + str(n))
print(count)