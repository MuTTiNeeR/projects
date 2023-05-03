try:
    class Calculator:
        def __init__(self):
            self.result = 0
            self.operators = ["+", "-", "*", "/", "clr", "q"]
        
        def showMenu(self):
            print(f"""
                ##########################
                ##      Calculator      ##
                ##########################
                #                        #
                ##########################
                #
                # Select the action you want to take:
                # "+"   ---> Addition
                # "-"   ---> Subtration
                # "*"   ---> Multiplication
                # "/"   ---> Division
                # "clr" ---> Clear
                # "q"   ---> Quit
                #
                ##########################
                ##########################
                
                Numer = {self.result}
                    
                ##########################         
                ##########################              
                """)
            
        def run(self):
            self.showMenu()
            choice = self.menuChoice()
            print(choice)
            
            if choice == "+":
                self.addition()
            elif choice == "-":
                self.subtration()
                pass
            elif choice == "*":
                self.multiplication()
                pass
            elif choice == "/":
                self.division()
                pass
            elif choice == "clr":
                self.clear()
                pass
            elif choice == "q":
                self.quit()            
        
        def menuChoice(self):
            while True:
                try:
                    operator = input("Select the math operation or quit 'q' : ").lower()
                    if operator not in self.operators:
                        raise ValueError
                    else:
                        return operator
                except:
                    print("Please select a valid transaction.")
                    
        def addition(self):
            if self.result == 0:
                while True:
                    try:
                        x = float(input("Enter the first number: "))
                        y = float(input("Enter the second number: "))
                        break
                    except ValueError:
                        print("Please enter a numeric value.")
                self.result += (x + y)
            else:
                while True:
                    try:
                        x = float(input("Enter the number: "))
                        break
                    except ValueError:
                        print("Please enter a numeric value.")
                self.result += x                        
            
        def subtration(self):
            if self.result == 0:
                while True:
                    try:
                        x = float(input("Enter the first number: "))
                        y = float(input("Enter the second number: "))
                        break
                    except ValueError:
                        print("Please enter a numeric value.")
                self.result += (x - y)
            else:
                while True:
                    try:
                        x = float(input("Enter the number: "))
                        break
                    except ValueError:
                        print("Please enter a numeric value.")
                self.result -= x
                
        def multiplication(self):
            if self.result == 0:
                while True:
                    try:
                        x = float(input("Enter the first number: "))
                        y = float(input("Enter the second number: "))
                        break
                    except ValueError:
                        print("Please enter a numeric value.")
                self.result += (x * y)
            else:
                while True:
                    try:
                        x = float(input("Enter the number: "))
                        break
                    except ValueError:
                        print("Please enter a numeric value.")
                self.result *= x
                
        def division(self):
            if self.result == 0:
                while True:
                    try:
                        x = float(input("Enter the first number: "))
                        y = float(input("Enter the second number: "))
                        self.result += (x / y)
                        break
                    except ValueError:
                        print("Please enter a numeric value.")
                    except ZeroDivisionError:
                        print("Cannot divide by zero. Please enter a non-zero value for the second number.")
            else:
                while True:
                    try:
                        x = float(input("Enter the number: "))
                        self.result /= x
                        break
                    except ValueError:
                        print("Please enter a numeric value.")
                    except ZeroDivisionError:
                        print("Cannot divide by zero. Please enter a non-zero value.")
                    
        def clear(self):
            self.result = 0                    
                    
        def quit(self):
            print("\nBye Bye...")
            quit()
 
    system = Calculator()
    
    while system:
        system.run()        
except KeyboardInterrupt:
    print("\nBye Bye...")
    quit()
