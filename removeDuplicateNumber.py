list_of_number = [1, 2, 2, 2, 3]

unique_list = []

for outer_number in range(len(list_of_number)):
	isDuplicate = False

	for inner_number in range(outer_number + 1, len(list_of_number)):
		if list_of_number[outer_number] == list_of_number[inner_number]:
			isDuplicate = True
			break

	if not isDuplicate:
		unique_list.append(list_of_number[outer_number])
					

print(unique_list)

# Alternative Method
full_name = "Dev Motors"
age = 4
employee_card = f"Employee: {full_name} & age is {age}"
print(employee_card)

print(3 + 3.4)

def greet():
    pass
    
print(greet()) # ?

example_list = ['example', 'dashed', 'name']

joined_str = ' '.join(example_list)
print(4 ** 4)  # ?

developer = 'Jessica'

print(developer.upper()) # JESSICA