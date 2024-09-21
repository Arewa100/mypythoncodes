from re import search

def email_validator(email):
    if search(r'\w+@\w+', email):
        return True
    else:
        raise ValueError("email must contain small letters and @ symbol")