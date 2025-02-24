import math

def square_root(x):
    return math.sqrt(x)

def factorial(x):
    return math.factorial(x)

def natural_log(x):
    return math.log(x)

def power(x, b):
    return math.pow(x, b)

def main():
    while True:
        print("\nScientific Calculator")
        print("1. Square Root")
        print("2. Factorial")
        print("3. Natural Logarithm")
        print("4. Power Function")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == '1':
            num = float(input("Enter number: "))
            print("Result:", square_root(num))
        elif choice == '2':
            num = int(input("Enter number: "))
            print("Result:", factorial(num))
        elif choice == '3':
            num = float(input("Enter number: "))
            print("Result:", natural_log(num))
        elif choice == '4':
            base = float(input("Enter base: "))
            exp = float(input("Enter exponent: "))
            print("Result:", power(base, exp))
        elif choice == '5':
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()

