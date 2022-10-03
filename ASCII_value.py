# Python program to print
# ASCII Value of Character

character = 'g'
# print the ASCII value of assigned character in c
print("The ASCII value of '" + character + "' is", ord(character))


print(4 *"\n")

print("Enter a String: ", end="")
text = input()
textlength = len(text)
for char in text:
	ascii = ord(char)
	print(char, "\t", ascii)
