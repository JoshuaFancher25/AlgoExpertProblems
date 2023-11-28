# we want to sort by value and by frequency of elements in an array.

array = [1, 1, 2, 2, 2, 7, 8]

dic = {}
for num in array:
    dic[num] = dic.get(num, 0) + 1

array.sort(key=lambda x: (dic[x], x))
print(array)
