number = int(input("Enter a number: "))

isPrime = True
if number == 1:
	isPrime = False

for count in range(2,number // 2 + 1):
	if number % count == 0:
		isPrime = False
		break

if isPrime:
	print("Prime Number")
else:
	print("Not a Prime Number")
