def analyze_logs(log_file):
    #create a suspicious ip dictionary
    suspicious_ips = {}

    #script to open the log file, read each line, flagged ips are extracted
    with open(log_file, 'r') as file:
        for line in file:
            if "401 - Failed login attempt" in line or "Suspicious Activity Detected":
                ip = line.split()[0]
                suspicious_ips[ip] = suspicious_ips.get(ip, 0) + 1
    #print header
    print("{:<15} {:<12}".format("IP Adress", "Occurences"))
    print("-" * 25)

    #Output
    for ip, count in suspicious_ips.items():
        print("{:<15} | {:<12}".format(ip, count))
    

# Sources:
# Week 3 Script Example
#Used ChatGPT to help with formatting the output, and using F strings. 
                
