# practice with short-circuiting in the while check
# since use use the "and" condition where both have to hold True
# if the first condition doesn't hold True we don't even have to
# check the second condition. The while loop will automatically break.

# Short-Circuiting - the evaluation of a compound expression stops as soon
#                    as the outcome is known, thus it doesn't matter that we
#                    we didn't define b 

def practiceShortCircuit(a):
    print("Program Running")
    while a < 10 and b == 100:
        print("infinte loop")

a = 11
practiceShortCircuit(a)