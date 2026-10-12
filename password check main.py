# bug and correct

password = input("Enter password: ")

has_upper = False
has_lower = False
has_digit = False

# Bug: Use len() to check the string length
if len(password) >= 8:
    for char in password:
        if char.isupper():
            has_upper = True  # Bug: Use assignment operator =
        elif char.islower():
            has_lower = True  # Bug: Use assignment operator =
        elif char.isdigit():
            has_digit = True  # Bug: Set to True when a digit is found

    # Bug: Use 'and' because all criteria are required
    if has_upper and has_lower and has_digit:
        print("Valid Password")
    else:
        print("Invalid Password")
else:
    print("Invalid Password")
