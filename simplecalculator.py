n1 = int(input("Enter the first number: \n"))  # convert input to integer
n2 = int(input("Enter the second number: \n"))  # convert input to integer

print("Select operation:\n")
print("1. Add\n2. Sub\n3. Div\n4. Multiply\n")

operator = int(input("Enter the operation: \n"))  # convert input to integer

if operator == 1:
    c = n1 + n2
    print("The addition is", c)
elif operator == 2:
    c = n1 - n2
    print("The subtraction is", c)
elif operator == 3:
    if n2 != 0:
        c = n1 / n2
        print("The division is", c)
    else:
        print("Error! Division by zero.")
elif operator == 4:
    c = n1 * n2
    print("The multiplication is", c)
else:
    print("Invalid input...!")
