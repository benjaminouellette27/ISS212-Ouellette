def analyze_logs(file_path, suspicious_ips):
    with open(file_path, 'r') as file:
        for line in file:
            for ip in suspicious_ips:
                for ip in line:
                    print(f"Suspicious activity detected from {ip}: ")
                    print(f"Log Entry: {line.strip()}")
                    print("-" * 30)
                    

def main():
    file_path = input("Enter a log file to analyze: ")
    input_ips = input("Enter IPs to flag for suspicious activity. For multiple IPs, seperate with commas:")
    suspicious_ips = [ip.strip() for ip in input_ips.split(',')]
    analyze_logs(file_path, suspicious_ips)
    

# Sources
# Week 3 Python Script Example
# Week 3 Powerpoint
# Used ChatGPT to help understand the line.strip
# Used ChatGPT to help debug lines 6 and 7 because the program would run, but no
# output was produced
