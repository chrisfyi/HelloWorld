for i in range(1, 13):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))

#number after the : is the formatting the width aka field width

print()
print()

# to left align put a < after the column
for i in range(1, 13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:<4}".format(i, i ** 2, i ** 3))

# < left align, >right align, ^center

print()

print("Pi is approximately {0:12}".format(22/7))
#f is a floating point value which is 6 digits after decimal
print("Pi is approximately {0:12f}".format(22/7))
# we add a precision of 50 points after the decimal
# precision is more important than field width and rejects the field width
print("Pi is approximately {0:12.50f}".format(22/7))
print("Pi is approximately {0:52.50f}".format(22/7))
print("Pi is approximately {0:62.50f}".format(22/7))
print("Pi is approximately {0:72.50f}".format(22/7))
print("Pi is approximately {0:<72.54f}".format(22/7))