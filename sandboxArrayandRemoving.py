# testing the process of removing in an array
array = [1,2,3,4,5,6,7,8,9]

print(len(array))
array[1] = None
print(array)
array.remove(5)
print(array)
# pop with an integer will remove the item from the array
# pop will also return the given item but we don't actually have to capture the item
# O(1) time
array.pop(1)
print(array)
# del will also remove the item
del array[1]
print(array)

# to help our understanding of a hashmap
# its consists of key:value pairs
# the key is hashed into the accompanying array via a hash function
# -- hash function is generally: key * prime_num % prime_num
# -- this type of hashing function helps minimize hashing collisions
# -- both the key and value are stored in the same location of the hashmap
# -- also: to mitigate hashing collisions it is generally and array of linked lists
# -- thus, if collision occurs we can add the value to the end of the linked list

dic = {"a": 100, "b": 200, "z": 5000, "hello": "world"}

print(dic)
print(dic["a"])

