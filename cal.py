class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

def main():
    calc = Calculator()
    while True:
        print("\nOptions:")
        print("Enter 'add' to add two numbers")
        print("Enter 'subtract' to subtract two numbers")
        print("Enter 'multiply' to multiply two numbers")
        print("Enter 'divide' to divide two numbers")
        print("Enter 'exit' to end the program")
        user_input = input(": ")

        if user_input == "exit":
            print("Exiting the program...")
            break
        elif user_input in ('add', 'subtract', 'multiply', 'divide'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if user_input == 'add':
                print("The result is", calc.add(num1, num2))
            elif user_input == 'subtract':
                print("The result is", calc.subtract(num1, num2))
            elif user_input == 'multiply':
                print("The result is", calc.multiply(num1, num2))
            elif user_input == 'divide':
                try:
                    print("The result is", calc.divide(num1, num2))
                except ValueError as e:
                    print(e)
        else:
            print("Unknown input")

if __name__ == "__main__":
    main()