# help with indexing in python
# learning the len function
array = [1,1,1,1,1]
print(len(array))
length = len(array)

# print(array[length]) ## causes an out of bounds since len is 5 but python is 0 indexed
for i in range(length):
    print(array[i])