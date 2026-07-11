string = input("Enter a string: ")
reverseString = ""

for char in string:
	reverseString = char + reverseString

if reverseString == string:
	print("Palindrome")
else:
	print("Not a Palindrome")

# Alternative Method
reverseText = string[::-1]

if reverseText == string:
	print("Palindrome")
else:
	print("Not a Palindrome")