string = input("Enter a string: ")

lower_case_count = 0
upper_case_count = 0

for char in string:
	if char.isupper():
		upper_case_count += 1
	elif char.islower(): 
		lower_case_count += 1

print("Upper Case Count: ",upper_case_count)
print("Lower Case Count: ",lower_case_count)