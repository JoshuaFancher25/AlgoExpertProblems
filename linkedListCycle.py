# for this problem we have two potential solutions
# 1.) we can use a set and keep track of all the nodes which have been seen
#     we check each head.next node being examined with set of nodes that have
#     already been seen, if we find a match then return True, a cycle exists
#     *** must make sure we increment the head for each iteration
# 2.) Floyds Tortoise and Hare Algorithm -
#     Utilize a fast and slow pointer, at some point the fast and slow pointer
#     will meet if a cycle exists in the linked list
#     ensure that we check for head == None and head.next == None, so that
#     the algorithm doesn't go out of bounds.

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # what i'm thinking is we can keep a set of all the nodes
        # we have seen before
        # if we see it again we know that we have a cycle
        nodeSet = set()

        while head != None:
            # create a set too keep track of all nodes seen

            # if the head node is in the set of nodes already then
            # we have already seen this node in the linked list
            # therefore, we have a cycle so return True
            if head in nodeSet:
                return True
            nodeSet.add(head)
            head = head.next
        # if we make it till the end of the list without finding
        # a duplicate node then we know we don't have a cycle
        # return False
        return False