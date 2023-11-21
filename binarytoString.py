# how to convert a number into binary representation

print(bin(10))
# will show Ob1010
# notice the Ob portion, critical to notice this detail

x = 10
x = bin(10)
print(x)
# must slice off the Ob portion of the string representation
print(x[2:])
x = x[2:]

# to convert back to an integer we use the built-in function int(string, 2)
# use the base = 2 in the int() function to properly convert
print(int(x,2))

# lets try converting a binary string with int() with the base 16 notation
# wow, it actually works as expected, can use big ff or little FF, works the same

y = "FF"
print(int(y, 16))