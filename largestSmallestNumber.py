list_of_number = [4, 8, 1, 9, 2]
smallest = list_of_number[0]
largest = list_of_number[0]

for number in list_of_number:
	# print(number)
	if number > largest:
		largest = number
	
	if number < smallest:
		smallest = number

print("Largest Number: ", largest)
print("Smallest Number: ", smallest)

#  Alternative Method:
smallestNumber = min(list_of_number)
largestNumber = max(list_of_number)

print("Largest Number: ", largestNumber)
print("Smallest Number: ", smallestNumber)