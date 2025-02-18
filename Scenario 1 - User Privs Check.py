#Sources
#Week 4 Tool Dev Walkthrough
#Week 3 PowerPoint

def main():
    
    #using a while loop so the user doesn't have to restart the program.
    while True:
    
    #prompt user to enter role
        role = input("Enter your role (admin, user, guest): ").strip().lower()

    #determine level of access
        if role == "admin":
            print("Access Level: Full privileges granted.")
            break
        elif role == "user":
            print("Access Level: Limited privileges granted.")
            break
        elif role == "guest":
            print("Access Level: Read-on;y access granted")
            break
        else:
            print(f"Invalid role entered: ({role}). Please choose from admin, user, or guest.")

if __name__ == "__main__":
    main()
