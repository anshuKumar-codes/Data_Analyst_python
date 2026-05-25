"""Write a program that acts as a simple security and data entry gate.

The Requirements:

Input Cleaning: Ask the user to enter their "User ID". If the user enters it with extra spaces (e.g., "  admin123  "), use .strip() to clean it.

Access Control:

If the User ID is "admin", print "Access Granted."

If the User ID is not "admin", print "Access Denied" and stop the program.

String Analysis (If Access is Granted):

Ask the user to enter a "Security Code".

Check if the code starts with "BCA" and ends with "78".

If both conditions are true, print "Identity Verified." Otherwise, print "Invalid Security Code.


"""

user_id=input("User ID: ").strip()
if user_id=="admin" or user_id=="ADMIN":
    print("Access granted")
    
    security_code=input("Security code: ").strip()
    if security_code.startswith("BCA") and security_code.endswith("263"):
        print("Identify verified")
    else:
        print("invalid security code")
    
    marks=int(input("Enter your marks"))
    if marks >= 90:
        print("Grade A")
    elif marks >= 70:
        print("Grade B")
    elif marks >= 40:
        print("Grade C")
    else:
        print("Fail")
else:
    print("access denied")

