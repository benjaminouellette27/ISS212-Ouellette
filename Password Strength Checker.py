def check_my_password_strength(password):
    
    strong_password = True
    
    if len(password) < 8:
        strong_password = False
        print("Weak: password is to short")
        
    if not any(char.isupper() for char in password):
        strong_password = False
        print("Weak: password must contain an uppercase letter.")
        
    if not any(char.islower() for char in password):
        strong_password = False
        print("Weak: password must contain a lowercase letter.")
        
    if not any(char.isdigit() for char in password):
        strong_password = False
        print("Weak: password must contain a digit.")
        
    if not any(char in "!@#$%^&*()-_=+<>?/[]" for char in password):
        strong_password = False
        print("Weak: password must contain a special character.")

    if strong_password:
        print("Password is Strong! Nice Job!")
    else:
        print("Password is Weak! Please improve!")

def main():
    password = input("Enter your password: ")
    check_my_password_strength(password)


# Sources
# Used ChatGPT to better use and understand the char command, also used it to help with producing the output for if the password was strong or weak.

