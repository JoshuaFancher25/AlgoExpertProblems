# dictionary counts

string = "asdfsdasdf;;;;;;lkj;lkqwernxzvzxqwer"

dict = {}
for element in string:
    dict[element] = dict.get(element,0) + 1

# sorting on the element and on the frequencies