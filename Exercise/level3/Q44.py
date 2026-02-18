'''Define a base AppError and three subclasses: ValidationError, DatabaseError, AuthError.
Write a function that raises each based on a string input. Catch them at different levels..'''


class AppError(Exception):
    pass

class ValidationError(AppError):
    pass

class DatabaseError(AppError):
    pass

class AuthError(AppError):
    pass

def process(input_type):
    if input_type == 'bad_data':
        raise ValidationError("Invalid data")
    elif input_type == 'db_fail':
        raise DatabaseError("Database error occurred")
    elif input_type == 'auth_fail':
        raise AuthError("Authentication failed")
    else:
        print("Process completed successfully!")

test_inputs = ['bad_data', 'db_fail', 'auth_fail', 'ok_data']

for inp in test_inputs:
    try:
        process(inp)
    except ValidationError as ve:
        print(f"Caught ValidationError: '{ve}'")
    except DatabaseError as de:
        print(f"Caught DatabaseError: '{de}'")
    except AuthError as ae:
        print(f"Caught AuthError: '{ae}'")
    except AppError as ae:
        print(f"Caught AppError: '{ae}'")
    except Exception as e:
        print(f"Caught unknown exception: {e}")
