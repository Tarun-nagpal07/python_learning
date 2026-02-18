'''Write a division function using try/except to handle ZeroDivisionError, ValueError (non-
numeric input), and a generic Exception. Print a friendly message for each.'''

def division(divider):
    try:
        value = 10/divider
        print("Value after division : ",value)
    except ZeroDivisionError:
        print("Cannot Divide by Zero")
    except ValueError:
        print("Invalid input")
    except TypeError:
        print("Unsopported Divider")
    except Exception as e:
        print(e)

division(10)
division(0)
division("abc")
division('a')
division([1,2])