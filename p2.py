# Simple Calculator in Python
====================================================

A simple calculator is a basic program that performs mathematical operations such as addition, subtraction, multiplication, and division. It's an essential tool for anyone who needs to perform calculations on the go.

### Features of the Calculator

The calculator will have the following features:

*   Addition: The sum of two numbers
*   Subtraction: The difference between two numbers
*   Multiplication: The product of two numbers
*   Division: The quotient of two numbers

### Code Implementation

Below is a simple Python implementation of the calculator.

```python
class Calculator:
    def add(self, num1, num2):
        """Return the sum of two numbers."""
        return num1 + num2

    def subtract(self, num1, num2):
        """Return the difference between two numbers."""
        return num1 - num2

    def multiply(self, num1, num2):
        """Return the product of two numbers."""
        return num1 * num2

    def divide(self, num1, num2):
        """Return the quotient of two numbers."""
        if num2 != 0:
            return num1 / num2
        else:
            raise ValueError("Cannot divide by zero.")

def main():
    calculator = Calculator()
    
    while True:
        print("\nSimple Calculator")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Quit")

        choice = input("Choose an operation (1-5): ")

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == '1':
                print(f"{num1} + {num2} = {calculator.add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {calculator.subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {calculator.multiply(num1, num2)}")
            else:
                try:
                    print(f"{num1} / {num2} = {calculator.divide(num1, num2)}")
                except ValueError as e:
                    print(e)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 5.")

if __name__ == "__main__":
    main()
```

### Explanation

The code above defines a `Calculator` class with methods for addition, subtraction, multiplication, and division. The `main()` function is the entry point of the program. It creates an instance of the `Calculator` class and provides a simple text-based interface to interact with it.

The calculator uses a while loop to continuously prompt the user for input until they choose to quit. Depending on the user's choice, it will either perform the chosen operation or raise an error if division by zero is attempted.

This code demonstrates the basic principles of object-oriented programming in Python and how to create reusable and maintainable code using classes and methods.