

def validate_numbers(a_str, b_str):
    try:
        a = float(a_str)
        b = float(b_str)
        return a, b
    except ValueError:
        raise ValueError("Invalid numbers entered.")

def validate_choice(choice_str):
    if choice_str not in ['1','2','3','4']:
        raise ValueError("Invalid menu choice.")
    return int(choice_str)

if __name__ == "__main__":
    print(validate_numbers("10","5"))   
    print(validate_choice("2"))         
