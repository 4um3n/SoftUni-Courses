def password_validator(password: str):
    result = []
    if len(password) not in range(6, 11):
        result.append(f"Password must be between 6 and 10 characters")
    
    if not password.isalnum():
        result.append(f"Password must consist only of letters and digits")
    
    digits = [d for d in password if d.isdigit()]
    if len(digits) < 2:
        result.append(f"Password must have at least 2 digits")
    
    return result


is_pass_valid = password_validator(input())
if len(is_pass_valid) == 0:
    print(f"Password is valid")
else:
    print('\n'.join(is_pass_valid)) 
