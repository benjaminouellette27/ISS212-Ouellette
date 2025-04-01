# Benjamin Ouellette
# CIS 212 Cybersecurity Scripting
# Resources
# -----------
#hostIP.py
#Scenario 3 Example Script
#used ChatGPT to help with formatting the scanTime, scanResults, f string formatting on line 66, and the while loop in the main function.

#importing the modules used
import socket, datetime

#A function to check if the domain named passed to the host variable is valid or not.
def amIValidChat(host):
    try:
        ip = socket.gethostbyname(host)
        return True, ip
    except socket.gaierror:
        return False, None

#function to perform port scanning
#sets scan results to an empty list.
#scans the ports on the ip passed in range of 20-26.
#adds a scanTime variable to add when each port was scanned
#appends each scan to the scanResults list with its status, port #, and time of scan.
def itsScanningTime(ip):
    scanResults = []

    print(f"Scanning {ip}... ")
    for port in range(20, 26):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((ip, port))

        scanTime = datetime.datetime.now().strftime("%Y-%m-%d %H-%M")

        if result == 0:
            scanResults.append({"port": port, "Status": "OPEN", "Time": scanTime})
        else:
            scanResults.append({"port": port, "Status": "CLOSED", "Time": scanTime})

        sock.close()

    #taking inspiration from hostIP.py.
    #creates a user prompt to select if the user wants the scan summary.
    #with error handling in case of misspelling or invalid entry.
    while True:
        print("Would you like to view the scan summary? ")
        print("1.) Yes")
        print("2.) No")

        choice = input("Enter choice: ")

        if choice == '1':
            Summary(scanResults)
            break
        elif choice == '2':
            print("Exiting...")
            break
        else:
            print("Invalid: please enter a valid response.")

#function to give summary of scan.
#prints the port scanned, along with its status (OPEN or CLOSED) and time at which it was scanned.
#prints a scan completetion time stamp after for loop.
def Summary(scanResults):
    print("\nScan Summary:")
    for result in scanResults:
        print(f"port {result['port']} is {result['Status']} (Scanned at {result['Time']})")

    print("\nScan Complete at:", datetime.datetime.now())

#main function, takes user input for domain, gets the ip for the domain, calls
#sets up a while loop to allow a user to enter the domain name.
#send the domain name to a function that checks if the domain is valid
#returns the domain ip if valid
#then runs the port scanning with the ip passed as its parameter.
def main():
    while True:
        host = input("Enter Domain: ")
        im_so_valid, ip = amIValidChat(host)
        if im_so_valid:
            print("Domain is VALID")
            itsScanningTime(ip)
            break
        else:
            print("Domain is NOT VALID. Please try again.")

if __name__ == "__main__":
    main()







