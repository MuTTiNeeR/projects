operators = ["+", "-", "*", "/"]
while True:
    # Number control.
    try:
        num1 = float(input("Enter first number: "))
    except ValueError:
        print("Please enter number.")
        continue
    
    # Operator control.
    operator = input("Choose operator (+, -, *, /): ")
    try:
        if operator not in operators:
            raise ValueError
    except ValueError:
        print("Invalid operator.")
        continue
      
    # Number control.  
    try:
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Please enter number.")
        continue
    
    # Simple mathematical operations.
    if operator == "+":
        print(num1 + num2)
    if operator == "-":
        print(num1 - num2)
    if operator == "*":
        print(num1 * num2)
    if operator == "/":
        # Check if the divisor is zero.
        try:
            bolum = num1 / num2
            print(bolum)
        except ZeroDivisionError:
            print("Division by zero error.")
            continue
    
    con = input("Do you want to do another calculation? (y/n): ")
    if con.lower() == "n":
        break
