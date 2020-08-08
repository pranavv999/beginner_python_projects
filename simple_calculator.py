print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")
while True:
	while True:
		try:
			choice = int(input("\nEnter your choice : "))
			break
		except:
			print("Invalid Choice")

	if (choice >= 1) and (choice <=4):
		
		while True:
			try:
				print("\nEnter two numbers")
				num1 = float(input("first number : "))
				num2 = float(input("second number : "))
				break
			except:
				print("\nInvalid Input")

		if (choice == 1):
			res = num1 + num2
			print(f"Result : {res}")

		elif (choice == 2):
			res = num1 - num2
			print(f"Result : {res}")

		elif (choice == 3):
			res = num1 * num2
			print(f"Result : {res}")

		else:
			res = num1 / num2
			print(f"Result : {res}")

	else:
		break
