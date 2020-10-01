letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[::-1]
print(backwards)

print()
# create a slice that produces qpo
print(letters[16:13:-1])

print()
# create a slice to creat edcba
print(letters[4::-1])

print()
# create a slice to produce the last 8 characters in reverse
print(letters[26:17:-1])
#or print(letters[:-9:-1])

#last 4 characters
print()
print(letters[-4:])
#last letter
print(letters[-1:])
#first letter
print(letters[:1])
