# Benjamin M Ouellette
# CIS 212
# Citations
# ----------
#Week 8 Tool Dev Example
#Used ChatGPT to debug my formatted output. And help understand what some of the
#Lines of code were doing (Lines: 10, 21, 25)

#imports the regular expressions module for python
import re

#load and read the log file.
with open("auth.log", 'r') as file:
    log_file_data = file.read()

#Regex pattern for failed login.
reg_pattern = r"Failed password .* from (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"

#by using the 're.findall' with the 'reg_pattern' and 'log_file_data' parameters
#it will return a list with all the failed ip addresses within the log data file.
suspicious_ips = re.findall(reg_pattern, log_file_data)

#Converts that list of IPs into a set, which helps in this scenario because when you
#a set automatically removes duplicates.
unique_ips = set(suspicious_ips)

#Header for Output.
header = "{:<15}".format("Suspicious IP Addresses")

#Header separator.
separator = "-" * 23

#prints the header and the separator.
print(header)
print(separator)

#for loop for print each IP from the unique IP set.
for ip in unique_ips:
    print("{:<15}".format(ip))



