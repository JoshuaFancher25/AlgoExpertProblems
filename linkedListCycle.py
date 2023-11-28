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