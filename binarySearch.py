# a function that takes in a sorted array and returns true if the value exists
# determine if the value exists
# 1.) pre-condition for binary search is a sorted array***
# 2.) binary search runs in O(nlogn) time
#     - at each iteration 1/2 of the remaining array is eliminated
#     - 1 billion values only take 30 operations to know if the value exists
#     - 2^10 =~ 100
#     - 2^20 =~ 1,000,000
#     - 2^30 =~ 1,000,000,000 = log(1,000,000,000)
def binarySearch(array, target):
    l = 0
    r = len(array) - 1 ### must remember what the len is returning

    while l <= r:
        middle = (l + r) //2
        if array[middle] == target:
            return True
        elif array[middle]  > target:
            r = middle - 1

        else:
            l = middle + 1

    return False


array = [1,2,3,4,5,6,7,8,9,10]

print(binarySearch(array, 100))

