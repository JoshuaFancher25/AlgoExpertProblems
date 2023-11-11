# This is an input class. Do not edit.
# we are given a linkedlist with at least 1 node
# we want to return the middle node
# if there are two middle nodes (even number of nodes) return the
# -- second node
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

head = LinkedList(10)
head.next = LinkedList(15)
head.next.next = LinkedList(20)
head.next.next.next = LinkedList(25)


def middleNode(linkedList):
    length = getLength(linkedList)
    middleValue = 0
    count = 0

    if length % 2 == 0:
        middleValue = int((length // 2))
    else:
        middleValue = int(length // 2)

    while count != middleValue:
        count += 1
        linkedList = linkedList.next
    return linkedList



def getLength(linkedList):
    length = 0
    while linkedList != None:
        length += 1
        linkedList = linkedList.next
    return length

x = middleNode(head)
print(x.value)