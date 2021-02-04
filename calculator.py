def addition(a, b):
    return float(a + b)

def subtraction(a, b):
    return float(a - b)

def multiplication(a, b):
    return float(a * b)

def division(a,b):
    try:
        return float((a // b))

    except ZeroDivisionError:
        print("Cannot divide by 0")

