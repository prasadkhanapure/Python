string = str(input("Enter a string: "))
reversedText = ""

for char in string:
	reversedText = char + reversedText
	print(char)

print(reversedText)

# Alternative Method
reverseText = "".join(reversed(string))
print(reverseText)

# Alternative Method
reverseString = string[::-1]
print(reverseString)

# Alternative Method
stringList = list(string)
stringList.reverse()
reversedTxt = "".join(stringList)
print(reversedTxt)
