'''Use regular expressions to validate: (a) a phone number in 0XX-XXXXXXX format, (b) a
date in DD/MM/YYYY, and (c) a password with at least 8 chars, 1 digit, 1 uppercase.'''

import re

def validate_number(number):
    exp = '0\d{2}-\d{7}'
    return re.fullmatch(exp,number)


def validate_date(date):
    exp = '(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-\d{4}'
    return re.fullmatch(exp,date)

# print(validate_date('19-02-1000'))

def validate_password(password):
    exp = '^(?=.*[A-Z])(?=.*\d).{8,}$'
    return re.fullmatch(exp,password)


# print(validate_password('whwhwhwh0A'))