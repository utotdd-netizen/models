"""
A simple calculator module with basic arithmetic operations.
"""


class Calculator:
    """A simple calculator class for performing arithmetic operations."""

    @staticmethod
    def add(a, b):
        """Add two numbers."""
        return a + b

    @staticmethod
    def subtract(a, b):
        """Subtract two numbers."""
        return a - b

    @staticmethod
    def multiply(a, b):
        """Multiply two numbers."""
        return a * b

    @staticmethod
    def divide(a, b):
        """Divide two numbers."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    @staticmethod
    def power(a, b):
        """Raise a to the power of b."""
        return a ** b

    @staticmethod
    def modulo(a, b):
        """Get the remainder of a divided by b."""
        if b == 0:
            raise ValueError("Cannot take modulo with zero")
        return a % b


def main():
    """Main function to run the calculator interactively."""
    calc = Calculator()
    
    print("=" * 50)
    print("Welcome to the Python Calculator!")
    print("=" * 50)
    print("\nAvailable operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (**)")
    print("6. Modulo (%)")
    print("7. Exit")
    print("\n" + "=" * 50)
    
    while True:
        try:
            operation = input("\nChoose an operation (1-7): ").strip()
            
            if operation == '7':
                print("Thank you for using the calculator. Goodbye!")
                break
            
            if operation not in ['1', '2', '3', '4', '5', '6']:
                print("Invalid choice. Please enter a number between 1 and 7.")
                continue
            
            # Get the operands
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            
            # Perform the operation
            if operation == '1':
                result = calc.add(num1, num2)
                print(f"\n{num1} + {num2} = {result}")
            elif operation == '2':
                result = calc.subtract(num1, num2)
                print(f"\n{num1} - {num2} = {result}")
            elif operation == '3':
                result = calc.multiply(num1, num2)
                print(f"\n{num1} * {num2} = {result}")
            elif operation == '4':
                result = calc.divide(num1, num2)
                print(f"\n{num1} / {num2} = {result}")
            elif operation == '5':
                result = calc.power(num1, num2)
                print(f"\n{num1} ** {num2} = {result}")
            elif operation == '6':
                result = calc.modulo(num1, num2)
                print(f"\n{num1} % {num2} = {result}")
        
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
