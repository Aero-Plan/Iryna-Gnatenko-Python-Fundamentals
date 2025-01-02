"""
A four-digit natural number is specified:
- find the product of the digits of this number
- write the number in reverse order
- in ascending order, you need to sort the numbers included in the given number
"""

#ask user for an input
number_string = input("Please input a four-digit natural number: ")
errorMessage = "This doesn't seem to be a four-digit natural number"

#check if the input is a four-digit natural number
if len(number_string) == 4:
	try:
		number_integer = int(number_string)
		if number_integer >= 1000:
			print(f"Awesome, {number_integer} is a four-digit natural number")
		else:
			print (f"{errorMessage}")
	except ValueError:
		print (f"{errorMessage}")
else:
	print (f"{errorMessage}")

#find the product of the digits of this number

if 'number_integer' in vars():
	digits = []
	while number_integer > 0:
		digits.append(number_integer % 10)  # Get the last digit
		number_integer //= 10               # Remove the last digit
	digits.reverse()  # Reverse the list to restore original order

	currentDigit = int(digits[0])
	product = 1

	for currentDigit in digits:
		product *= currentDigit

	print(f"The product of digits {digits} is {product}")
