# mergeSort

def mergeSort(array):
    if len(array) <= 1:
        return array
    left_sorted = mergeSort(array[0:len(array)//2])
    right_sorted = mergeSort(array[len(array)//2:len(array)])
    return merge(left_sorted, right_sorted)

def merge(left, right):
    i = 0
    j = 0
    c = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            c.append(left[i])
            i += 1
        else:
            c.append(right[j])
            j += 1
    if i < len(left):
        c += left[i:]
    if j < len(right):
        c += right[j:]
    return c

array = [1,2,3,10,100,5,9,25,50,13,14]

print(mergeSort(array))

