# Two Sum Brute Force Time - O(n^2)
#                     Space - O(n) - no additional space is needed
# return the indices
array = [1,2,3,4,5,19]
target = 9

def two_sum(array, target):
    length = len(array)
    for i in range(0,length - 1):
        for j in range(i+1, length):
            if array[i] + array[j] == target:
                return [i, j ]
    return []

print(two_sum(array, target))

# TwoSum Optimal Solution - O(n) - only on pass through the array is needed
#                           O(n) - space is O(n) have to create a dictionary
#                                - space directly scales with input size n
def twoSum(nums, target):
    dictionary = {}

    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in dictionary:
            return [dictionary[complement], i]
        else:
            dictionary[nums[i]] = i
    return []


print(twoSum(array, target))