array = [1,10,2,4,3,7,8]
d = 10

def triplet_modulus(array, d):
    array.sort()
    length = len(array)
    count = 0
    if len(array) < 3:
        return 0
    for i in range(length-2):
        for j in range(i+1, length-1):
            for k in range(j+1, length):
                triplet_sum = array[i] + array[j] + array[k]
                if (triplet_sum % d) == 0:
                    count += 1
    return count

print(triplet_modulus(array,d))