# topRow = ["a", "b", "c", "d"]
# bottomRow = ["e", "f", "g", "h"]
keyboard = [["a", "b", "c", "d"], ["e", "f", "g", "h"]]
dic = {}


for i in range(len(keyboard)):
    for j in range(len(keyboard[i])):
        dic[i, j] = keyboard[i][j]

print(dic)
# can't use the enhanced for loop must use
# indices for slicing