number = int(input("Enter a number: "))

factorial_number = 1

for count in range(1, number + 1):
	factorial_number *= count

print(factorial_number)