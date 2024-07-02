import re

def check_password_strength(password):
    score = 0
    suggestions = []

    # check length
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Password should be at least 8 characters long")

    # check for uppercase letter
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Password should contain at least one uppercase letter")

    # check for lowercase letter
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Password should contain at least one lowercase letter")

    # check for numeric digit
    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Password should contain at least one numeric digit")

    # check for special character
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        suggestions.append("Password should contain at least one special character (!@#$%^&*(),.?\":{}|<>)")

    return score, suggestions
password = input("Input a password: ")
print(check_password_strength(password))
