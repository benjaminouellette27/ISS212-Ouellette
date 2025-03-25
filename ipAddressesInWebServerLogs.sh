# Benjamin M Ouellette
# CIS 212
# Citations
# ----------
#Week 8 example script
#Used ChatGPT to debug line 18, and to check and correct my syntax.
#Used the site Stack Overflow to learn about string operators, and correct my syntax on line 32.


#setting my log_file variable.
log_file="access.log"

#added a nice output here to show whats happening in the script.
#learned about the -e option to add spcaing to the script for a better flowing and looking output.
echo -e "\nCounting IP addresses to be redacted..."

#using the grep along with the E and o parameters to enable regualr expression and only print the matched expressions.
#then piping that output to word count command with -1 optiuon to count the numnber of Ip addresses found.
ip_count=$(grep -Eo '[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+' "$log_file" | wc -l)

#using the sed command and regular expressions wit#!/bin/bashh the -E option.
#This line goes through the log file and replaces all IP addresses with the string
# [REDACTED], and then saves all IP addresses redacted this way to a new log file.
echo -e "\nRedacting IP Addresses..."
sed -E 's/[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+/[REDACTED]/g' $log_file > access_redacted.log

#Same as line 13, adding ways to see what the script is doing, and makes for a better output.
#Also printing the number of found IP addresses within the log file.
echo -e "\nNumber of IP Addresses, found and redacted: $ip_count"

#using the '%' operator to remove the suffix from the log file, and adding '_redacted.log' to the string.
echo "Redacted IP addresses in $log_file file, and saved as ${log_file%.log}_redacted.log"
