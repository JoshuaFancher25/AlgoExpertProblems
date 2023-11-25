# counting a binary string

x = "11000"
print(x.count("1"))
y = 10
count = 0
while y > 0:
    if (10 % 2) == 0:
        count += 1
        y = y % 2
    else:
        y = y % 2
print(count)