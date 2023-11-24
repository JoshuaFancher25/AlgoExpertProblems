
def findDisappearedNumbers(nums):
    length = len(nums)
    output = []
    dic = {}
    for num in nums:
        dic[num] = True
    for i in range(1,length + 1):
        if i not in dic:
            output.append(i)
    return output

nums = [1,1]
print(findDisappearedNumbers(nums))