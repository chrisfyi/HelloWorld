age = 29

#turns age into a string with the str operator
print("My age is " + str(age) + " years")

# {} is the replacement field
print("My age is {0} years".format(age))

# There are 8 replacement fields and will replace the fields in the.format
print("There are {0} days in {1}, {2}, {3}, {4}, {5} , {6}, and {7}"
      .format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))

print("There are {0} days in Jan, Mar, May, Jul, Aug, Oct, Dec".format(31))

#replaces the replacement field with the according replacement
print("Jan: {2}, Feb: {0}, Mar: {2}, Jun: {1}, Jul: {2}, Sep: {1}, Oct:{2}, Nov: {1}, Dec: {2}"
      .format(28, 30, 31))

print()

print("""Jan: {2}
          Feb: {0}
          Mar: {2}
          Jun: {1}
          Jul: {2}
          Sep: {1}
          Oct: {2}
          Nov: {1}
          Dec: {2}
          """.format(28, 30, 31))


