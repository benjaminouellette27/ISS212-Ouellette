def main():
    protocol = input("Enter the protocol name: ")
    if protocol == "Cyphersec":
        print("Cyphersec is the only supported protocol!")
    elif protocol == "cybersec":
        print("DENIED. Cyphersec protocol ONLY!")
    else:
        print(f"Cyphersec! Not {protocol}!")

main()

# Sources
# Week 3 Script examples
