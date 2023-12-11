# dictionary is an array and a hashing function
# the key is hashed to an integer
# the integer then represents the place to store the value in the hashtable
# hash tables have efficient lookup, insert, delete operations
# hashing collision can occur -
# good hash function can be some modulus operator with an prime number and possibly
# multiplying the key by a prime number as well 

array = ["a", "a", "b", "c", "d", "d", "d", "d", "d", "e", "e"]

dic = {}
for letter in array:
    dic[letter] = dic.get(letter, 0) + 1
print(dic)

# this will iterate over the keys
for element in dic:
    print(element)

# singular call will result in the keys being iterated over
for element in dic:
    print(dic[element])

# must unpack the tuple at each iteration that is returned by dic.items()
print("Printing an unpacked tuple of key value pairs ---")
for key, value in dic.items():
    print(key + " " + str(value))

# other ways to iterate over a dictionary - just the keys being iterated over
print("Printing Keys")
for key in dic.keys():
    print(key)

# iterate over just the values in a dictionary
print("Printing Values ")
for value in dic.values():
    print(value)