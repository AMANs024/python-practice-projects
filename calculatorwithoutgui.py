def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def power(a, b):
    return a ** b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero not allowed")
    return a / b

def multiply(a, b):
    return a * b


def calculator():
    print("A simple calculator for Arithmetic operations (CLI)")
    print("Use +, -, *, /, ^ for calculations")
    
    while True:
        expr = input("Enter an expression (or 'q' to exit): ").strip()
        
        if expr.lower() == 'q':
            print("Exiting the calculator ......")
            break

        try:
            if '+' in expr:
                a, b = expr.split('+')
                print(add(float(a), float(b)))
            elif '-' in expr:
                a, b = expr.split('-')
                print(subtract(float(a), float(b)))
            elif '*' in expr:
                a, b = expr.split('*')
                print(multiply(float(a), float(b)))
            elif '/' in expr:
                a, b = expr.split('/')
                print(divide(float(a), float(b)))
            elif '^' in expr:
                a, b = expr.split('^')
                print(power(float(a), float(b)))
            else:
                print("Invalid expression")

        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    calculator()
