#
# variable assignment
# tuple packing and unpacking
# a tuple is implicitly created on the right hand side of the equals
# - the tuple is then unpacked on the left hand side of the equals
# - tuples are immutable - they cannot be modified after creation

a = 5
b = 10

a, b = b, a

print(a)

a_tuple = a, b
print(a_tuple)