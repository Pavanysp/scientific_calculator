import math

def square_root(x):
    return math.sqrt(x)

def factorial(x):
    return math.factorial(x)

def natural_log(x):
    return math.log(x)

def power(x, y):
    return math.pow(x, y)

def main():
    import sys
    
    # Check if running in a non-interactive environment (Jenkins)
    is_automated = len(sys.argv) > 1 and sys.argv[1] == "--auto"
    
    # Predefined inputs for Jenkins (automated mode)
    predefined_inputs = iter(["1", "16", "2", "5", "3", "10", "4", "2", "3", "5"])
    
    while True:
        print("\nScientific Calculator")
        print("1. SquareRoot")
        print("2. Factorial")
        print("3. Natural Logarithm")
        print("4. Power Function")
        print("5. Exit")
        
        if is_automated:
            choice = next(predefined_inputs, "5")  # Default to "5" if out of inputs
            print(f"Simulated choice: {choice}")
        else:
            choice = input("Enter choice (1-5): ")

        if choice == "1":
            num = float(input("Enter number: ")) if not is_automated else float(next(predefined_inputs))
            print(f"Square Root of {num} is: {square_root(num)}")
        elif choice == "2":
            num = int(input("Enter number: ")) if not is_automated else int(next(predefined_inputs))
            print(f"Factorial of {num} is: {factorial(num)}")
        elif choice == "3":
            num = float(input("Enter number: ")) if not is_automated else float(next(predefined_inputs))
            print(f"Natural Log of {num} is: {natural_log(num)}")
        elif choice == "4":
            base = float(input("Enter base: ")) if not is_automated else float(next(predefined_inputs))
            exponent = float(input("Enter exponent: ")) if not is_automated else float(next(predefined_inputs))
            print(f"{base} to the power {exponent} is: {power(base, exponent)}")
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
