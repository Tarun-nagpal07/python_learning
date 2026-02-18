
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

if __name__ == "__main__":
    print("Testing operations.py")
    print("Add 2+3 =", add(2,3))
    print("Divide 10/2 =", divide(10,2))
