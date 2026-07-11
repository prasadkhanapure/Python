string = str(input("Enter a string: "))

# vowels = ["a", "e", "i", "o", "u"]
# Need to above way too

total = 0

for count in range(len(string)):
	if string[count] == "a" or string[count] == "e" or string[count] == "i" or string[count] == "o" or string[count] == "u":
		total += 1

print(total)

# Alternative Method

total = 0
vowels = ["a", "e", "i", "o", "u"]

for char in string:
	if char in vowels:
		total += 1

print(total)