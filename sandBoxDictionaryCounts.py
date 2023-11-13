# dictionary counts

string = "asdfsdasdf;;;;;;lkj;lkqwernxzvzxqwer"

dict = {}
for element in string:
    dict[element] = dict.get(element,0) + 1
print(dict)
# sorting on the element and on the frequencies
print(dict.get(";"))

# dictionary consists of key value pairs
# really a dictionary is a hashing function and an array
# the hashing function tells us which element to access in the array
# hashing function can be something simple such as a modular
# f(h) = h * 11 % m;
# where m is prime number 