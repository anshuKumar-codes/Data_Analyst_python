# Password Validator (Strings & Conditionals)

# Task: Store a "secret password" in a variable (e.g., secret = "Python123"). Ask the user to input a password.

# Logic: * If it matches exactly, print "Access Granted".

# If it doesn't match, print "Access Denied".

# Check if the user's input is too short (less than 5 characters) and warn them

password=input("Enter password: ")

if password=="python123".upper():
    print("Access granted")
elif len(password)<=5:
    print("Password is more than 5 character")
else:
    print("Access denied")