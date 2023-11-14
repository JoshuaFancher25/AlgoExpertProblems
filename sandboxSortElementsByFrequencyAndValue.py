
# sort by value and sort by frequency
# simplest version
# modified mergeSort is a better version in my opinion

array = [1,1,3,4,5,7,8,9,2,2,2]
dict = {}

for num in array:
    dict[num] = dict.get(num, 0) + 1

array.sort(key = lambda x : (dict[x], x))

print(array)