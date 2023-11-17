dictionary = {}

dictionary["hello"] = True
dictionary["world"] = False
dictionary["class"] = 100
dictionary["nothing"] = True

if True in dictionary:
    print("True")
else:
    print("False")